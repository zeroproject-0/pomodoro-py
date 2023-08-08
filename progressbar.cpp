#include "progressbar.h"

Progressbar::Progressbar(QWidget* parent, QWidget* progressbar)
{
	this->parent = parent;
	this->progressbar = progressbar;
	width = 260;
	height = 260;
	progress_width = 5;
	max_value = 100;
	progress_color = QColor(255, 121, 198);
	shadow = NULL;
	bg_color = QColor(68, 71, 90, 140);

	add_shadow();
}

void Progressbar::set_value(int value)
{
	currentProgress = value;

	this->parent->repaint();
}

void Progressbar::add_shadow()
{
	shadow = new QGraphicsDropShadowEffect();
	shadow->setBlurRadius(15);
	shadow->setXOffset(0);
	shadow->setYOffset(5);
	shadow->setColor(QColor(0, 0, 0, 120));

	this->progressbar->setGraphicsEffect(shadow);
}

void Progressbar::paintProgress()
{
	// Parameters
	int width = this->width - this->progress_width;
	int height = this->height - this->progress_width;
	int margin_top = (this->progress_width / 2) + 30;
	int margin_left = (this->progress_width / 2) + 20;
	int progress = this->currentProgress * 360 / this->max_value;

	// Painter
	QPainter paint = QPainter();
	paint.begin(this->parent);
	paint.setRenderHint(QPainter::Antialiasing);

	// Create Rectangle
	QRect rect = QRect(0, 0, this->width, this->height);
	paint.setPen(Qt::NoPen);
	paint.drawRect(rect);

	// Create Pen
	QPen pen = QPen();
	pen.setWidth(this->progress_width);

	pen.setColor(this->bg_color);
	paint.setPen(pen);
	paint.drawArc(margin_left, margin_top, width, height, 0, 360 * 16);


	pen.setColor(this->progress_color);

	pen.setCapStyle(Qt::RoundCap);

	// Create arc
	paint.setPen(pen);
	paint.drawArc(margin_left, margin_top, width, height, 90 * 16, progress * 16);

	paint.end();
}

