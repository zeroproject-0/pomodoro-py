#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_mainwindow.h"
#include "ui_MainWindowSmall.h";
#include "progressbar.h"
#include "settingswindow.h"
#include <QMenu>
#include <QSystemTrayIcon>

class MainWindow : public QMainWindow
{
	Q_OBJECT

public:
	MainWindow(QWidget* parent = nullptr);
	~MainWindow();
	void displayCounterTime(int);

	Progressbar* progressbar;

protected:
	void paintEvent(QPaintEvent*) override;
	void mousePressEvent(QMouseEvent*) override;
	void mouseMoveEvent(QMouseEvent*) override;
	void enterEvent(QEnterEvent*) override;
	void leaveEvent(QEvent*) override;
	void contextMenuEvent(QContextMenuEvent*) override;

private slots:
	void on_actionButton_clicked();
	void on_stopButton_clicked();
	void on_btnExit_clicked();
	void on_btnMinimize_clicked();
	void on_btnOpenSettings_clicked();
	void on_btnIcon_clicked();

	void tray_open_settings();
	void tray_always_top();
	void tray_minimize();
	void tray_exit();

	void updateTimer();
	void updateSettings();

private:
	Ui::MainWindowClass ui;

	void start();
	QString parseDisplayTime(int);
	void load_settings();
	void reset_timer(int);
	void open_settings();
	void toggle_always_top();

	bool isHideTitleBarActive;
	bool isAutoStartRestTimeActive;
	bool isPomoTime;
	bool isAlwaysTop;
	QString GROUP;
	QTimer* timer;
	int current_time;
	int pomo_time;
	int rest_time;
	int repeats;

	QSystemTrayIcon* tray_icon;
	QMenu* context_menu;
	QPoint circle_position;
	QPoint* old_position;
};

class MainWindowSmall : public QMainWindow
{
	Q_OBJECT

public:
	MainWindowSmall(QWidget* parent = nullptr);
	~MainWindowSmall();
	void displayCounterTime(int);

	Progressbar* progressbar;

protected:
	void paintEvent(QPaintEvent*) override;
	void mousePressEvent(QMouseEvent*) override;
	void mouseMoveEvent(QMouseEvent*) override;
	void contextMenuEvent(QContextMenuEvent*) override;

private slots:
	void on_btnExit_clicked();
	void on_btnMinimize_clicked();
	void on_btnOpenSettings_clicked();
	void on_btnIcon_clicked();

	void tray_open_settings();
	void tray_always_top();
	void tray_minimize();
	void tray_exit();

	void updateTimer();
	void updateSettings();

private:
	Ui::MainWindowSmall ui;

	QAction* start_action;
	QAction* stop_action;

	void start();
	QString parseDisplayTime(int);
	void load_settings();
	void reset_timer(int);
	void open_settings();
	void toggle_always_top();
	void stop();

	bool isHideTitleBarActive;
	bool isAutoStartRestTimeActive;
	bool isPomoTime;
	bool isAlwaysTop;
	QString GROUP;
	QTimer* timer;
	int current_time;
	int pomo_time;
	int rest_time;
	int repeats;

	QSystemTrayIcon* tray_icon;
	QMenu* context_menu;
	QPoint circle_position;
	QPoint* old_position;

};
