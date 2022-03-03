from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from utils import Settings
from ui import Ui_Settings


class SettingsWindow(QDialog):
  def __init__(self, parent) -> None:
    QDialog.__init__(self, parent)
    self.ui = Ui_Settings()
    self.ui.setupUi(self)

    self.settings = Settings.get_instance()

    self.setWindowTitle("Settings")

    self.setWindowFlag(Qt.FramelessWindowHint, True)
    self.setAttribute(Qt.WA_TranslucentBackground)

    minute_validator = QIntValidator(0, 99)
    second_validator = QRegularExpression(r"^[0-9]|[1-5][0-9]$")

    self.ui.leMinutes.setValidator(minute_validator)
    self.ui.leSeconds.setValidator(
        QRegularExpressionValidator(second_validator))

    self.ui.btnSave.clicked.connect(self.save_settings)
    self.ui.btnCancel.clicked.connect(self.close)
    self.ui.cbHideTitleBar.setChecked(self.settings.auto_hide_title_bar)
    self.ui.leMinutes.setText(str(self.settings.time // 60))
    self.ui.leSeconds.setText(str(self.settings.time % 60))

  def save_settings(self) -> None:
    self.settings.auto_hide_title_bar = self.ui.cbHideTitleBar.isChecked()
    self.settings.time = int(self.ui.leMinutes.text()) * \
        60 + int(self.ui.leSeconds.text())
    self.settings.save()
    self.accept()

  def close(self) -> None:
    self.reject()
