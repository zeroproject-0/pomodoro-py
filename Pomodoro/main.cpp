#include "mainwindow.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    a.setApplicationName("Pomodoro");
    a.setApplicationVersion("1.0");
    a.setOrganizationName("zeroproject");
    a.setOrganizationDomain("zeroproject.dev");
    MainWindow w;
    w.show();
    return a.exec();
}
