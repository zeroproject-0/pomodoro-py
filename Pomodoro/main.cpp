#include "mainwindow.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    a.setApplicationName("Pomodoro");
    a.setApplicationVersion("1.1.0");
    a.setOrganizationName("zeroproject");
    a.setOrganizationDomain("https://zeroproject.dev");
    a.setWindowIcon(QIcon(QString(":/Logo/assets/Pomodoro.ico")));

    MainWindow w;
    w.show();
    return a.exec();
}
