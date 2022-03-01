# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsGZNooK.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(500, 200)
        Settings.setMinimumSize(QSize(500, 200))
        Settings.setMaximumSize(QSize(500, 200))
        Settings.setStyleSheet(u"QPushButton {\n"
"	width: 100px;\n"
"	height: 25px;\n"
"	color: rgb(151, 159, 200);\n"
"	background-color: rgb(68, 71, 90);\n"
"	border-radius: 12px;\n"
"	font: 18px;\n"
"}\n"
"      \n"
"QPushButton:hover:!pressed {\n"
"	background-color: rgb(151, 159, 200);\n"
"	color:  rgb(68, 71, 90);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	border: #fff;\n"
"}")
        Settings.setWindowFilePath(u"")
        self.verticalLayout_4 = QVBoxLayout(Settings)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(Settings)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"QFrame {\n"
"	background-color: #282a36;\n"
"	color: #f8f8f2;\n"
"	border-radius: 15px;\n"
"	font: 12pt \"Ubuntu\";\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.container.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.time = QFrame(self.container)
        self.time.setObjectName(u"time")
        self.time.setFrameShape(QFrame.NoFrame)
        self.time.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.time)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.time)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.time)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leMinutes = QLineEdit(self.frame_2)
        self.leMinutes.setObjectName(u"leMinutes")
        self.leMinutes.setMinimumSize(QSize(130, 25))
        self.leMinutes.setMaximumSize(QSize(100, 25))
        self.leMinutes.setLayoutDirection(Qt.LeftToRight)
        self.leMinutes.setText(u"")
        self.leMinutes.setMaxLength(2)
        self.leMinutes.setFrame(False)
        self.leMinutes.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.leMinutes.setPlaceholderText(u"Minutes (max 99)")
        self.leMinutes.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.leMinutes)

        self.leSeconds = QLineEdit(self.frame_2)
        self.leSeconds.setObjectName(u"leSeconds")
        self.leSeconds.setMinimumSize(QSize(130, 25))
        self.leSeconds.setMaximumSize(QSize(100, 25))
        self.leSeconds.setText(u"")
        self.leSeconds.setMaxLength(2)
        self.leSeconds.setFrame(False)
        self.leSeconds.setCursorPosition(0)
        self.leSeconds.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.leSeconds.setPlaceholderText(u"Seconds (max 59)")

        self.horizontalLayout_2.addWidget(self.leSeconds)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.time)

        self.frame = QFrame(self.container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.cbHideTitleBar = QCheckBox(self.frame)
        self.cbHideTitleBar.setObjectName(u"cbHideTitleBar")
        self.cbHideTitleBar.setMinimumSize(QSize(20, 0))
        self.cbHideTitleBar.setMaximumSize(QSize(20, 16777215))
        self.cbHideTitleBar.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbHideTitleBar.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	background-color: rgba(189, 147, 249, 145);\n"
"	border: none;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	background-color: #ff79c6;\n"
"	border: none;\n"
"}")
        self.cbHideTitleBar.setChecked(True)

        self.horizontalLayout_3.addWidget(self.cbHideTitleBar)


        self.verticalLayout_2.addWidget(self.frame)

        self.buttons = QFrame(self.container)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(self.buttons)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 25))
        self.btnCancel.setMaximumSize(QSize(100, 25))
        self.btnCancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.buttons)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 25))
        self.btnSave.setMaximumSize(QSize(100, 25))
        self.btnSave.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout_2.addWidget(self.buttons)


        self.verticalLayout_4.addWidget(self.container)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Time:", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Auto Hide Title bar:", None))
        self.cbHideTitleBar.setText("")
        self.btnCancel.setText(QCoreApplication.translate("Settings", u"Cancel", None))
        self.btnSave.setText(QCoreApplication.translate("Settings", u"Save", None))
    # retranslateUi

