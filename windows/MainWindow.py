import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import *

# Forms
from ui.ui_main import Ui_Pomodoro

# import circular_progress
from widgets import PomodoroProgress
from widgets import Counter

from utils import Settings

from .SettingsWindow import SettingsWindow

settings = Settings.get_instance()


class MainWindow(QMainWindow):
  def __init__(self) -> None:
    global settings
    QMainWindow.__init__(self)
    self.ui = Ui_Pomodoro()
    self.ui.setupUi(self)

    self.setWindowIcon(QIcon("./assets/Logo.ico"))

    self.ui.title.setVisible(not settings.auto_hide_title_bar)

    # Initial time
    self.TOTAL_TIME = settings.time if settings.time > 0 else 25 * 60
    self.current_time = 0
    self.timer = QTimer()

    # Remove title bar
    self.setWindowFlag(Qt.FramelessWindowHint, True)
    self.setWindowFlag(Qt.WindowStaysOnTopHint, settings.alway_on_top)
    self.ui.cbAlwaysOnTop.setChecked(settings.alway_on_top)
    self.setAttribute(Qt.WA_TranslucentBackground)

    # Add counter
    self.counter = Counter()
    self.counter.setParent(self.ui.container)
    self.counter.set_value(self.TOTAL_TIME)
    self.counter.move(95, 100)
    self.counter.show()

    # Create circular progress
    self.progress = PomodoroProgress()
    self.progress.setFixedSize(self.progress.width, self.progress.height)
    self.progress.move(20, 5)
    self.progress.add_shadow(True)
    self.progress.font_size = 40
    self.progress.bg_color = QColor(68, 71, 90, 140)
    self.progress.setParent(self.ui.container)
    self.progress.show()

    # Add button
    self.pressed_button = False
    self.add_action_button()

    # Events
    self.ui.centralwidget.setAttribute(Qt.WA_Hover)
    self.ui.btnExit.clicked.connect(self.close)

    self.ui.btnMinimize.clicked.connect(self.minimized)

    self.ui.btnSettings.clicked.connect(self.open_settings)

    # Always on top
    self.ui.cbAlwaysOnTop.stateChanged.connect(self.set_always_on_top)

    # Add drop shadow
    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(15)
    self.shadow.setXOffset(0)
    self.shadow.setYOffset(0)
    self.shadow.setColor(QColor(0, 0, 0, 120))
    self.setGraphicsEffect(self.shadow)

    # show window
    self.show()

  def open_settings(self):
    self.settings = SettingsWindow(self)
    r = self.settings.exec()
    self.ui.title.setVisible(True)
    if r == QDialog.Accepted:
      self.reset_timer()
      self.TOTAL_TIME = settings.time
      self.progress.set_value(0)
      self.counter.set_value(self.TOTAL_TIME)

  def minimized(self):
    self.showMinimized()

  def set_always_on_top(self, event):
    settings.alway_on_top = self.ui.cbAlwaysOnTop.isChecked()
    self.setWindowFlag(Qt.WindowStaysOnTopHint, settings.alway_on_top)
    settings.save()
    self.show()

  def mouse_press_event(self, event: QMouseEvent):
    self.oldPosition = event.globalPosition().toPoint()

  def mouse_move_event(self, event: QMouseEvent):
    delta = QPoint(event.globalPosition().toPoint() - self.oldPosition)
    self.move(self.x() + delta.x(), self.y() + delta.y())
    self.oldPosition = event.globalPosition().toPoint()

  # add button
  def add_action_button(self):
    self.button = QPushButton("Start", self)
    self.button.setStyleSheet("""QPushButton {
                                  width: 100px;
                                  height: 25px;
                                  color: rgb(151, 159, 200);
                                  background-color: rgb(68, 71, 90);
                                  font-size: 18px;
                                  border-radius: 12px;}
      
                                QPushButton:hover:!pressed {
                                  background-color: rgb(151, 159, 200);
                                  color:  rgb(68, 71, 90);}""")
    self.button.setCursor(Qt.PointingHandCursor)
    self.button.move(self.ui.container.width() / 2 - self.button.width() / 2,
                     self.ui.container.height()/2 + self.button.height() + 10)
    self.button.clicked.connect(self.start_timer)
    self.button.setParent(self.ui.container)
    self.button.show()

  # start timer
  def start_timer(self):
    self.pressed_button = ~self.pressed_button
    self.button.setText("Stop" if self.pressed_button else "Start")
    if self.pressed_button:
      self.current_time = 0
      self.timer = QTimer()
      self.timer.timeout.connect(self.update)
      if ~self.timer.isActive():
        self.timer.start()
    else:
      self.reset_timer()

  def close(self):
    sys.exit()

  def event(self, event):
    if settings.auto_hide_title_bar:
      if event.type() == QEvent.HoverEnter:
        self.ui.title.showNormal()
      elif event.type() == QEvent.HoverLeave:
        self.ui.title.hide()
    if event.type() == QEvent.MouseButtonPress:
      self.mouse_press_event(event)
    elif event.type() == QEvent.MouseMove:
      self.mouse_move_event(event)
    return super().event(event)

  def update(self):

    self.timer.setInterval(1000)

    self.progress.set_value(self.current_time * 100 / self.TOTAL_TIME)
    self.counter.set_value(self.TOTAL_TIME - self.current_time)

    if self.current_time >= self.TOTAL_TIME:
      self.reset_timer()
      url = QUrl.fromLocalFile("./assets/sounds/1-sound.wav")
      audio_output = QAudioOutput()
      audio_output.setVolume(80)
      player = QMediaPlayer()
      player.setAudioOutput(audio_output)
      player.setSource(url)
      player.setLoops(2)
      player.play()
      self.show_message("Time is up!", "Good Job!",
                        "Do you want to start again?")

    self.current_time += 1

  def finished(self):
    print("finished")

  def show_message(self, title, text, message):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(QMessageBox.Question)
    msg.setInformativeText(message)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setDefaultButton(QMessageBox.Ok)

    msg.buttonClicked.connect(self.message_button)

    x = msg.exec()

  def message_button(self, event):
    if event.text().upper() == "&OK" or event.text().upper() == "OK":
      self.start_timer()

  def reset_timer(self):
    self.button.setText("Start")
    self.pressed_button = False
    self.counter.set_value(self.TOTAL_TIME)
    self.progress.set_value(0)
    self.timer.stop()
