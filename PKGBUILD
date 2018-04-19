# Script generated with Bloom
pkgdesc="ROS - rqt_image_view provides a GUI plugin for displaying images using image_transport."
url='http://wiki.ros.org/rqt_image_view'

pkgname='ros-kinetic-rqt-image-view'
pkgver='0.4.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-cpp'
'ros-kinetic-sensor-msgs'
)

depends=('ros-kinetic-cv-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-cpp'
'ros-kinetic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=rqt_image_view
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_image_view $srcdir/rqt_image_view
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

