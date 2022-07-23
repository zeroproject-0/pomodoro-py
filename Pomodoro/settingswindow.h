#pragma once

#include <QDialog>
#include <QtCore>
#include <QDebug>
#include <QSettings>

#include "ui_settingswindow.h"
#include "settings.h"

class SettingsWindow : public QDialog
{
	Q_OBJECT

public:
	SettingsWindow(QWidget *parent = nullptr);
	~SettingsWindow();

private slots:
	void on_btnSave_clicked();
	void on_btnCancel_clicked();

private:
	Ui::SettingsWindowClass ui;
	void load_settings();
};
