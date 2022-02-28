# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainbVWAyz.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Pomodoro(object):
  def setupUi(self, Pomodoro):
    if not Pomodoro.objectName():
      Pomodoro.setObjectName(u"Pomodoro")
    Pomodoro.resize(300, 300)
    Pomodoro.setMinimumSize(QSize(300, 300))
    Pomodoro.setMaximumSize(QSize(300, 300))
    font = QFont()
    font.setPointSize(16)
    Pomodoro.setFont(font)
    self.centralwidget = QWidget(Pomodoro)
    self.centralwidget.setObjectName(u"centralwidget")
    self.verticalLayout = QVBoxLayout(self.centralwidget)
    self.verticalLayout.setSpacing(0)
    self.verticalLayout.setObjectName(u"verticalLayout")
    self.verticalLayout.setContentsMargins(10, 10, 10, 10)
    self.container = QFrame(self.centralwidget)
    self.container.setObjectName(u"container")
    self.container.setFrameShape(QFrame.NoFrame)
    self.container.setFrameShadow(QFrame.Sunken)
    self.verticalLayout_2 = QVBoxLayout(self.container)
    self.verticalLayout_2.setSpacing(0)
    self.verticalLayout_2.setObjectName(u"verticalLayout_2")
    self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
    self.circle_bg = QFrame(self.container)
    self.circle_bg.setObjectName(u"circle_bg")
    self.circle_bg.setStyleSheet(u"QFrame {\n"
                                 "	background-color: #282a36;\n"
                                 "	color: #f8f8f2;\n"
                                 "	border-radius: 120px;\n"
                                 "	font: 12pt \"Ubuntu\";\n"
                                 "}")
    self.circle_bg.setFrameShape(QFrame.NoFrame)
    self.circle_bg.setFrameShadow(QFrame.Raised)
    self.verticalLayout_3 = QVBoxLayout(self.circle_bg)
    self.verticalLayout_3.setSpacing(0)
    self.verticalLayout_3.setObjectName(u"verticalLayout_3")
    self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
    self.texts = QFrame(self.circle_bg)
    self.texts.setObjectName(u"texts")
    self.texts.setMaximumSize(QSize(16777215, 160))
    self.texts.setStyleSheet(u"background: none;")
    self.texts.setFrameShape(QFrame.NoFrame)
    self.texts.setFrameShadow(QFrame.Raised)
    self.verticalLayout_4 = QVBoxLayout(self.texts)
    self.verticalLayout_4.setSpacing(0)
    self.verticalLayout_4.setObjectName(u"verticalLayout_4")
    self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
    self.gridLayout = QGridLayout()
    self.gridLayout.setSpacing(0)
    self.gridLayout.setObjectName(u"gridLayout")
    self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
    self.frame = QFrame(self.texts)
    self.frame.setObjectName(u"frame")
    self.frame.setMaximumSize(QSize(16777215, 16777215))
    self.frame.setFrameShape(QFrame.NoFrame)
    self.frame.setFrameShadow(QFrame.Raised)
    self.verticalLayout_5 = QVBoxLayout(self.frame)
    self.verticalLayout_5.setSpacing(0)
    self.verticalLayout_5.setObjectName(u"verticalLayout_5")
    self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

    self.gridLayout.addWidget(self.frame, 2, 0, 1, 1, Qt.AlignBottom)

    self.label = QLabel(self.texts)
    self.label.setObjectName(u"label")
    self.label.setMaximumSize(QSize(16777215, 30))
    font1 = QFont()
    font1.setFamily(u"Ubuntu")
    font1.setBold(True)
    font1.setItalic(False)
    font1.setWeight(QFont.Bold)
    self.label.setFont(font1)
    self.label.setStyleSheet(u"font-size: 24px;\n"
                             "font: bold;")
    self.label.setText(u"Pomodoro")
    self.label.setAlignment(Qt.AlignCenter)

    self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

    self.verticalLayout_4.addLayout(self.gridLayout)

    self.verticalLayout_3.addWidget(self.texts)

    self.verticalLayout_2.addWidget(self.circle_bg)

    self.verticalLayout.addWidget(self.container)

    Pomodoro.setCentralWidget(self.centralwidget)

    self.retranslateUi(Pomodoro)

    QMetaObject.connectSlotsByName(Pomodoro)
  # setupUi

  def retranslateUi(self, Pomodoro):
    Pomodoro.setWindowTitle(
        QCoreApplication.translate("Pomodoro", u"Pomodoro", None))
  # retranslateUi
