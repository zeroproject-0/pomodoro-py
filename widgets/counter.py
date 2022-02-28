from venv import create
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Counter(QWidget):
  def __init__(self):
    QWidget.__init__(self)

    self.width = 200
    self.height = 50
    self.style_sheet = "border:none;min-width: 50px;min-height: 50px;color: #fff;"
    self.segment_style = QLCDNumber.Flat
    self.digit_count = 2
    self.setStyleSheet("background-color: transparent;border: 1px solid #fff;")

    self.separator = self.create_separator()

    self.minutes = self.create_counter()
    self.seconds = self.create_counter()

    self.seconds.move(self.minutes.width()-40, 0)
    self.separator.move(self.minutes.width()-50, 0)

  def create_counter(self):
    counter = QLCDNumber(self)
    counter.setStyleSheet(self.style_sheet)
    counter.setMode(QLCDNumber.Dec)
    counter.setSegmentStyle(self.segment_style)
    counter.setDigitCount(self.digit_count)

    return counter

  def create_separator(self):
    separator = QLabel(self)
    separator.setStyleSheet(
        "color: #fff;font: 31pt \"Ubuntu\";border: none;")
    separator.setText(":")

    return separator

  def set_value(self, value):
    minutes = value // 60
    seconts = value % 60

    self.minutes.display(self.parse_display(minutes))
    self.seconds.display(self.parse_display(seconts))

  def parse_display(self, value):
    return "0"+str(value) if value < 10 else value
