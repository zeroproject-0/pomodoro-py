# Maintainer: zeroproject <contact@zeroproject.dev>
pkgname=zomodoro
pkgver=2.0.0
pkgrel=1
pkgdesc="Simple pomodoro made in Qt"
arch=('x86_64')
url="https://github.com/zeroproject-dev/zomodoro"
license=('MIT')
depends=('qt6-base')
makedepends=('git', 'qmake', 'make')
source=('zomodoro::git://github.com/zeroproject-dev/zomodoro.git')
md5sums=('SKIP')

pkgver() {
	cd "$pkgname"
	git describe --tags
}

build() {
	cd "$pkgname-$pkgver"
	./configure --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	install -Dm755 ./zomodoro "$pkgdir/usr/bin/zomodoro"
	install -Dm644 ./README.md "$pkgdir/usr/share/doc/$pkgname"
}
