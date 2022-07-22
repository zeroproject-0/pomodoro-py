#include <QWidget>
#include <QtGui>
#include <QtCore>
#include <QGraphicsDropShadowEffect>

class Progressbar
{

public:
	Progressbar(QWidget* parent = nullptr, QWidget* progressbar = nullptr);
	void set_value(int);
	void add_shadow();
	void paintProgress();

	int width;
	int height;
	int progress_width;
	int max_value;
	QColor progress_color;
	QGraphicsDropShadowEffect* shadow;
	QColor bg_color;
	QWidget* parent;
	QWidget* progressbar;

private:
	int currentProgress;
};

