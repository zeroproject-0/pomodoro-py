# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkbJHCI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

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
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(0, 30, 300, 270))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.container.setMinimumSize(QSize(300, 270))
        self.container.setMaximumSize(QSize(300, 270))
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.circle_bg = QFrame(self.container)
        self.circle_bg.setObjectName(u"circle_bg")
        sizePolicy.setHeightForWidth(self.circle_bg.sizePolicy().hasHeightForWidth())
        self.circle_bg.setSizePolicy(sizePolicy)
        self.circle_bg.setMinimumSize(QSize(240, 240))
        self.circle_bg.setMaximumSize(QSize(240, 240))
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
        self.label = QLabel(self.texts)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font-size: 24px;\n"
"font: bold;")
        self.label.setText(u"Pomodoro")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

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


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.texts)


        self.horizontalLayout_2.addWidget(self.circle_bg)

        self.title = QFrame(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 300, 25))
        self.title.setMinimumSize(QSize(300, 25))
        self.title.setMaximumSize(QSize(300, 25))
        self.title.setStyleSheet(u"QFrame#title {\n"
"	background-color: #282a36;\n"
"	color: #f8f8f2;\n"
"	border-radius: 12px;\n"
"}")
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.title)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(25, 25))
        self.label_3.setMaximumSize(QSize(25, 25))
        self.label_3.setPixmap(QPixmap(u"../assets/Logo.ico"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_3)

        self.btnSettings = QPushButton(self.title)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(25, 25))
        self.btnSettings.setMaximumSize(QSize(25, 25))
        self.btnSettings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSettings.setStyleSheet(u"QPushButton {\n"
"	width: 100px;\n"
"	height: 25px;\n"
"	color: rgb(151, 159, 200);\n"
"	background-color: rgb(68, 71, 90);\n"
"	font: 18px;\n"
"	border: none;\n"
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
        self.btnSettings.setText(u"S")
        self.btnSettings.setAutoDefault(False)
        self.btnSettings.setFlat(False)

        self.horizontalLayout.addWidget(self.btnSettings)

        self.label_2 = QLabel(self.title)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: #f8f8f2;")

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.cbAlwaysOnTop = QCheckBox(self.title)
        self.cbAlwaysOnTop.setObjectName(u"cbAlwaysOnTop")
        self.cbAlwaysOnTop.setMinimumSize(QSize(15, 25))
        self.cbAlwaysOnTop.setMaximumSize(QSize(15, 25))
        self.cbAlwaysOnTop.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbAlwaysOnTop.setToolTipDuration(1)
        self.cbAlwaysOnTop.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	background-color: rgba(189, 147, 249, 145);\n"
"	border: none;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	background-color: #ff79c6;\n"
"	border: none;\n"
"}")
        self.cbAlwaysOnTop.setChecked(False)
        self.cbAlwaysOnTop.setTristate(False)

        self.horizontalLayout.addWidget(self.cbAlwaysOnTop, 0, Qt.AlignVCenter)

        self.btnMinimize = QPushButton(self.title)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(25, 25))
        self.btnMinimize.setMaximumSize(QSize(25, 25))
        self.btnMinimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMinimize.setStyleSheet(u"QPushButton#btnMinimize {\n"
"	background-color: #282a36;\n"
"	color: #f8f8f2;\n"
"	border: none;\n"
"}")

        self.horizontalLayout.addWidget(self.btnMinimize)

        self.btnExit = QPushButton(self.title)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(25, 25))
        self.btnExit.setMaximumSize(QSize(25, 25))
        self.btnExit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExit.setStyleSheet(u"QPushButton#btnExit {\n"
"	background-color: #282a36;\n"
"	color: #f8f8f2;\n"
"	border-radius: 12px;\n"
"}")

        self.horizontalLayout.addWidget(self.btnExit)

        Pomodoro.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pomodoro)

        self.btnSettings.setDefault(False)


        QMetaObject.connectSlotsByName(Pomodoro)
    # setupUi

    def retranslateUi(self, Pomodoro):
        Pomodoro.setWindowTitle(QCoreApplication.translate("Pomodoro", u"Pomodoro", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("Pomodoro", u"Pomodoro - zeroproject", None))
#if QT_CONFIG(tooltip)
        self.cbAlwaysOnTop.setToolTip(QCoreApplication.translate("Pomodoro", u"Always on top", None))
#endif // QT_CONFIG(tooltip)
        self.cbAlwaysOnTop.setText("")
        self.btnMinimize.setText(QCoreApplication.translate("Pomodoro", u"_", None))
        self.btnExit.setText(QCoreApplication.translate("Pomodoro", u"x", None))
    # retranslateUi

