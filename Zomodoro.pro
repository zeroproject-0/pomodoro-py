QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

HEADERS += ./progressbar.h \
    ./settings.h \
		./mainwindow.h \
		./settingswindow.h
SOURCES += ./progressbar.cpp \
    ./settings.cpp \
		./settingswindow.cpp \
		./mainwindow.cpp \
		./main.cpp
FORMS += ./mainwindow.ui \
    ./settingswindow.ui \
    ./mainwindowsmall.ui
RESOURCES += mainwindow.qrc

win32:RC_FILE = Zomodoro.rc

qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
