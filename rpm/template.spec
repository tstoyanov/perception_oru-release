Name:           ros-hydro-perception-oru
Version:        1.0.24
Release:        0%{?dist}
Summary:        ROS perception_oru package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/perception_oru
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-ndt-feature-reg
Requires:       ros-hydro-ndt-fuser
Requires:       ros-hydro-ndt-map
Requires:       ros-hydro-ndt-map-builder
Requires:       ros-hydro-ndt-mcl
Requires:       ros-hydro-ndt-registration
Requires:       ros-hydro-ndt-rviz-visualisation
Requires:       ros-hydro-ndt-visualisation
Requires:       ros-hydro-sdf-tracker
BuildRequires:  ros-hydro-catkin

%description
Perception packages from the MRO lab at AASS, Orebro University

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Nov 25 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.24-0
- Autogenerated by Bloom

* Tue Nov 25 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.23-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.22-0
- Autogenerated by Bloom

