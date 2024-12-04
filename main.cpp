#include "mainwindow.h"
#include "settings.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[]) {
  QApplication a(argc, argv);
  a.setApplicationName("Zomodoro");
  a.setApplicationVersion("2.0.0");
  a.setOrganizationName("zeroproject");
  a.setOrganizationDomain("https://zeroproject.dev");
  a.setWindowIcon(QIcon(QString(":/Logo/assets/Pomodoro.ico")));

  bool isSmall =
      Settings::load_settings("is_small", false, "MainWindow").value<bool>();

  if (isSmall) {
    MainWindowSmall *w = new MainWindowSmall();
    w->show();
  } else {
    MainWindow *w = new MainWindow();
    w->show();
  }

  return a.exec();
}
