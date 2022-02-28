import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Forms
from ui_main import Ui_Pomodoro

# import circular_progress
from widgets import PomodoroProgress
from widgets import Counter

# Globals
counter = 0


class MainWindow(QMainWindow):
  def __init__(self) -> None:
    QMainWindow.__init__(self)
    self.ui = Ui_Pomodoro()
    self.ui.setupUi(self)

    # Remove title bar
    self.setWindowFlag(Qt.FramelessWindowHint, True)
    self.setAttribute(Qt.WA_TranslucentBackground)

    # Add counter
    self.counter = Counter()
    self.counter.set_value(120)
    self.counter.setParent(self.ui.container)
    self.counter.move(95, 120)
    self.counter.setStyleSheet("background-color: #f00;")
    self.counter.show()

    # Create circular progress
    self.progress = PomodoroProgress()
    self.progress.value = 50
    self.progress.setFixedSize(self.progress.width, self.progress.height)
    self.progress.move(20, 20)
    self.progress.add_shadow(True)
    self.progress.font_size = 40
    # self.progress.bg_color = QColor(68, 71, 90, 140) #TODO Implement background color for progress bar
    self.progress.setParent(self.ui.container)
    self.progress.show()

    # Events
    self.ui.centralwidget.setAttribute(Qt.WA_Hover)
    self.ui.btnExit.clicked.connect(self.close)

    # Add drop shadow
    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(15)
    self.shadow.setXOffset(0)
    self.shadow.setYOffset(0)
    self.shadow.setColor(QColor(0, 0, 0, 120))
    self.setGraphicsEffect(self.shadow)

    # show window
    self.show()

  def close(self):
    sys.exit()

  def event(self, event):
    if event.type() == QEvent.HoverEnter:
      print("enter")
    elif event.type() == QEvent.HoverLeave:
      print("leave")
    return super().event(event)

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
  sys.exit(app.exec())
