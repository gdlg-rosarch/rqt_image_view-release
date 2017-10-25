Name:           ros-lunar-rqt-image-view
Version:        0.4.11
Release:        0%{?dist}
Summary:        ROS rqt_image_view package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_image_view
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-cv-bridge
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-rqt-gui
Requires:       ros-lunar-rqt-gui-cpp
Requires:       ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cv-bridge
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-rqt-gui
BuildRequires:  ros-lunar-rqt-gui-cpp
BuildRequires:  ros-lunar-sensor-msgs

%description
rqt_image_view provides a GUI plugin for displaying images using
image_transport.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Oct 25 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.11-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.10-0
- Autogenerated by Bloom

* Thu Jul 27 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.9-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.8-0
- Autogenerated by Bloom

