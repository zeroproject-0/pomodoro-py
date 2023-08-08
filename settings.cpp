#include "settings.h"

void Settings::save_settings(const QString& key, const QVariant& value, const QString& group)
{
	QSettings settings;
	settings.beginGroup(group);
	settings.setValue(key, value);
	settings.endGroup();
}

QVariant Settings::load_settings(const QString& key, const QVariant& def_value, const QString& group)
{
	QVariant value;
	QSettings settings;
	settings.beginGroup(group);
	value = settings.value(key, def_value);
	settings.endGroup();
	return value;
}
