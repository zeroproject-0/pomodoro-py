#include "mainwindow.h"
#include <QScreen>

MainWindow::MainWindow(QWidget* parent)
	: QMainWindow(parent)
{
	ui.setupUi(this);

	setWindowFlag(Qt::FramelessWindowHint);
	setAttribute(Qt::WA_TranslucentBackground);
	setAttribute(Qt::WA_NoSystemBackground);

	GROUP = "MainWindow";

	progressbar = new Progressbar(this, ui.progressBar);
	timer = new QTimer();
	QObject::connect(timer, &QTimer::timeout, this, &MainWindow::updateTimer);

	current_time = 0;
	progressbar->set_value(current_time);
	load_settings();

	context_menu = new QMenu();

	QAction* settings_action = new QAction("Settings");
	QObject::connect(settings_action, &QAction::triggered, this, &MainWindow::tray_open_settings);
	context_menu->addAction(settings_action);

	QAction* always_top_action = new QAction("Always on top");
	QObject::connect(always_top_action, &QAction::triggered, this, &MainWindow::tray_always_top);
	always_top_action->setCheckable(true);
	always_top_action->setChecked(isAlwaysTop);
	context_menu->addAction(always_top_action);

	QAction* web_action = new QAction("Web");
	QObject::connect(web_action, &QAction::triggered, this, [] {QDesktopServices::openUrl(QUrl("https://zeroproject.dev"));});
	context_menu->addAction(web_action);
	context_menu->addSeparator();

	QAction* minimize_action = new QAction("Minimize");
	QObject::connect(minimize_action, &QAction::triggered, this, &MainWindow::tray_minimize);
	context_menu->addAction(minimize_action);

	QAction* exit_action = new QAction("Exit");
	QObject::connect(exit_action, &QAction::triggered, this, &MainWindow::tray_exit);
	context_menu->addAction(exit_action);

	if (QSystemTrayIcon::isSystemTrayAvailable()) {
		tray_icon = new QSystemTrayIcon(this);

		tray_icon->setIcon(QIcon(QString::fromUtf8(":/Logo/assets/Pomodoro.ico")));
		tray_icon->setToolTip(QString("Pomodoro - zeroproject"));
		tray_icon->setContextMenu(context_menu);
		tray_icon->show();
	}
}

MainWindow::~MainWindow()
{
	delete timer;
	delete progressbar;
	delete context_menu;
	delete tray_icon;
}

void MainWindow::displayCounterTime(int total_time)
{
	int time = total_time - current_time;
	int minutes = time / 60;
	int seconds = time % 60;

	QString minutes_formated = parseDisplayTime(minutes);
	QString seconds_formated = parseDisplayTime(seconds);

	ui.minutes->display(minutes_formated.toLatin1());
	ui.seconds->display(seconds_formated.toLatin1());
}

void MainWindow::start()
{
	if (timer->isActive()) {
		timer->stop();
		ui.actionButton->setIcon(QIcon(":/Icons/assets/play.png"));
	}
	else {
		timer->start();
		ui.actionButton->setIcon(QIcon(":/Icons/assets/pause.png"));
	}
}

QString MainWindow::parseDisplayTime(int time) {
	QString stime = QString::number(time);
	return time < 10 ? "0" + stime : stime;
}

void MainWindow::load_settings()
{
	pomo_time = Settings::load_settings("pomo_time", 1500, "SettingsWindow").value<int>();
	rest_time = Settings::load_settings("rest_time", 300, "SettingsWindow").value<int>();
	isAlwaysTop = Settings::load_settings("always_top", false, GROUP).value<bool>();
	this->setWindowFlag(Qt::WindowStaysOnTopHint, isAlwaysTop);

	isHideTitleBarActive = Settings::load_settings("hide_title_bar", false, "SettingsWindow").value<bool>();
	isAutoStartRestTimeActive = Settings::load_settings("auto_start_rest_time", true, "SettingsWindow").value<bool>();

	ui.frame->setVisible(!isHideTitleBarActive);
	ui.frame_2->setVisible(!isHideTitleBarActive);

	isPomoTime = true;

	displayCounterTime(pomo_time);
}

void MainWindow::reset_timer(int total_time)
{
		timer->stop();
		ui.lbTimeTitle->setText(isPomoTime ? "Work Time" : "Rest Time");
		current_time = 0;
		ui.actionButton->setIcon(QIcon(":/Icons/assets/play.png"));
		progressbar->set_value(current_time);
		displayCounterTime(total_time);
}

void MainWindow::open_settings()
{
	if (timer->isActive()) {
		timer->stop();
		ui.actionButton->setIcon(QIcon(":/Icons/assets/play.png"));
	}

	SettingsWindow* settingsWindow = new SettingsWindow(this);

	settingsWindow->setModal(true);
	settingsWindow->show();

	QObject::connect(settingsWindow, &QDialog::accepted, this, &MainWindow::updateSettings);
}

void MainWindow::toggle_always_top()
{
	isAlwaysTop = !isAlwaysTop;
	Settings::save_settings("always_top", isAlwaysTop, GROUP);

	this->setWindowFlag(Qt::WindowStaysOnTopHint, isAlwaysTop);
	this->show();
}

void MainWindow::paintEvent(QPaintEvent* e)
{
	progressbar->paintProgress();
	e->accept();
}

void MainWindow::mousePressEvent(QMouseEvent* e)
{
	QPointF pos = e->globalPos();
	old_position = new QPoint((int)pos.x(), (int)pos.y());
}

void MainWindow::mouseMoveEvent(QMouseEvent* e)
{
	QPoint* delta = new QPoint(e->globalPos() - *old_position);
	this->move(this->x() + delta->x(), this->y() + delta->y());
	*old_position = e->globalPos();
}

void MainWindow::enterEvent(QEnterEvent*)
{
}

void MainWindow::leaveEvent(QEvent*)
{
}

void MainWindow::contextMenuEvent(QContextMenuEvent* e)
{
	(context_menu->exec(e->globalPos()));
}

void MainWindow::on_btnExit_clicked()
{
	this->close();
}

void MainWindow::on_btnMinimize_clicked()
{
	this->showMinimized();
}

void MainWindow::on_btnOpenSettings_clicked()
{
	open_settings();
}

void MainWindow::on_btnIcon_clicked()
{
	QDesktopServices::openUrl(QUrl(QApplication::organizationDomain()));
}

void MainWindow::tray_open_settings()
{
	open_settings();
}

void MainWindow::tray_always_top()
{
	toggle_always_top();
}

void MainWindow::tray_minimize()
{
	this->showMinimized();
}

void MainWindow::tray_exit()
{
	this->close();
}

void MainWindow::updateTimer()
{
	int time = isPomoTime ? pomo_time : rest_time;
	timer->setInterval(1000);
	progressbar->set_value(current_time * progressbar->max_value / time);
	this->displayCounterTime(time);

	if (current_time >= time) {
		isPomoTime = !isPomoTime;
		time = isPomoTime ? pomo_time : rest_time;
		reset_timer(time);

		if(QSystemTrayIcon::isSystemTrayAvailable())
			tray_icon->showMessage(QString("Pomodoro"), QString("Time Finished"), QSystemTrayIcon::Information, 5000);

		if (isAutoStartRestTimeActive && !isPomoTime) {
			start();
		}
	}

	current_time += 1;
}

void MainWindow::updateSettings()
{
	load_settings();
	reset_timer(pomo_time);
}

void MainWindow::on_actionButton_clicked()
{
	this->start();
}

void MainWindow::on_stopButton_clicked()
{
	isPomoTime = true;
	this->reset_timer(pomo_time);
}


