pkgname=yay-faster-cn
pkgver=0.11
pkgrel="2"
pkgdesc="Use github mirror to speed yay up in China."
arch=('any')
url="https://github.com/iamzhz/yay-faster-cn"
license=('MIT')


depends=('python' 'python-setuptools' 'git' 'wget' 'yay')
makedepends=('python-setuptools')


source=("https://github.com/iamzhz/yay-faster-cn/releases/download/v${pkgver}/yay_faster_cn_v${pkgver}.tar.gz")
sha256sums=('30266b4ab777f56d917ba355db4a1c38ba844de2e8a506fc8d902feebd714d5d')

build() {
  cd "$pkgname-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$pkgname-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}