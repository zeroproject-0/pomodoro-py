import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Forms
from ui_main import Ui_Pomodoro

# import circular_progress
from widgets import PomodoroProgress

# Globals
counter = 0


class MainWindow(QMainWindow):
  def __init__(self) -> None:
    QMainWindow.__init__(self)
    self.ui = Ui_Pomodoro()
    self.ui.setupUi(self)

    # Remove title bar
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setAttribute(Qt.WA_TranslucentBackground)

    # Create circular progress
    self.progress = PomodoroProgress()
    self.progress.width = 270
    self.progress.height = 270
    self.progress.value = 0
    self.progress.setFixedSize(self.progress.width, self.progress.height)
    self.progress.move(15, 15)
    self.progress.add_shadow(True)
    self.progress.font_size = 40
    # self.progress.bg_color = QColor(68, 71, 90, 140) #TODO Implement background color for progress bar
    # self.progress.setParent(self.ui.centralwidget)
    # self.progress.show()

    # Add drop shadow
    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(15)
    self.shadow.setXOffset(0)
    self.shadow.setYOffset(0)
    self.shadow.setColor(QColor(0, 0, 0, 120))
    self.setGraphicsEffect(self.shadow)

    # Start button
    self.ui.btnAction.clicked.connect(self.btnActionClick)

    # show window
    self.show()

  def btnActionClick(self, button):
    # Qtimer
    self.timer = QTimer()
    self.timer.timeout.connect(self.update)
    self.timer.start(25)

  def update(self):
    global counter

    # Set value to progress bar
    self.progress.set_value(counter)

    # Finish timer
    if counter >= 100:
      # stop timer
      self.timer.stop()

    # Increase counter
    counter += 1


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec_())
