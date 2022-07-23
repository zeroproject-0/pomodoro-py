#pragma once
#include <QtCore/qmap.h>
#include <QtCore/qjsonobject.h>
#include "mainwindow.h"
#include <QSettings>

class Settings
{
public:
	static void save_settings(const QString&, const QVariant&, const QString&);
	static QVariant load_settings(const QString&, const QVariant&, const QString&);

private:
};

