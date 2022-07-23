#include "settingswindow.h"

SettingsWindow::SettingsWindow(QWidget *parent)
	: QDialog(parent)
{
	ui.setupUi(this);

	setWindowFlag(Qt::FramelessWindowHint);
	setAttribute(Qt::WA_TranslucentBackground);
	setAttribute(Qt::WA_NoSystemBackground);

	load_settings();
}

SettingsWindow::~SettingsWindow()
{}

void SettingsWindow::on_btnSave_clicked()
{
	QString GROUP = "SettingsWindow";
	int pomo_time = ui.sbPMinutes->value() * 60 + ui.sbPSeconds->value();
	int rest_time = ui.sbRMinutes->value() * 60 + ui.sbRSeconds->value();

	Settings::save_settings("pomo_time", pomo_time, GROUP);
	Settings::save_settings("rest_time", rest_time, GROUP);
	Settings::save_settings("hide_title_bar", ui.cbAutoHideTitleBar->isChecked(), GROUP);
	Settings::save_settings("auto_start_rest_time", ui.cbAutoStartRestTime->isChecked(), GROUP);

	this->accept();
}

void SettingsWindow::on_btnCancel_clicked()
{
	this->reject();
}

void SettingsWindow::load_settings()
{
	QString GROUP = "SettingsWindow";

	int pomo_time = Settings::load_settings("pomo_time", 1500, GROUP).value<int>();
	int rest_time = Settings::load_settings("rest_time", 300, GROUP).value<int>();
	bool hide_title_bar = Settings::load_settings("hide_title_bar", false, GROUP).value<bool>();
	bool auto_start_rest_time = Settings::load_settings("auto_start_rest_time", false, GROUP).value<bool>();
	
	ui.sbPMinutes->setValue(pomo_time / 60);
	ui.sbPSeconds->setValue(pomo_time % 60);
	ui.sbRMinutes->setValue(rest_time / 60);
	ui.sbRSeconds->setValue(rest_time % 60);
	ui.cbAutoHideTitleBar->setChecked(hide_title_bar);
	ui.cbAutoStartRestTime->setChecked(auto_start_rest_time);
}
