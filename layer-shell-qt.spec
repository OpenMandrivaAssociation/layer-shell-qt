%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define major 5

Name:		layer-shell-qt
Version:	5.22.0
Release:	1
Summary:	Qt component to allow applications to make use of the Wayland wl-layer-shell protocol
Group:		System/Libraries
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/libkcompactdisc
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5WaylandClient)
BuildRequires:	cmake(Qt5XkbCommonSupport)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	qt5-qtwayland

%description
Qt component to allow applications to make use of the Wayland wl-layer-shell protocol

%files
%dir %{_libdir}/qt5/plugins/wayland-shell-integration
%{_libdir}/qt5/plugins/wayland-shell-integration/liblayer-shell.so
# No need to split this into a package of its own, the library is useless
# without the Qt plugin
%{_libdir}/libLayerShellQtInterface.so.%{major}*

#------------------------------------------------------------------------------
%define devname %mklibname LayerShellQtInterface -d

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Qt component to allow applications to make use of the Wayland wl-layer-shell protocol

%files -n %{devname}
%{_libdir}/libLayerShellQtInterface.so
%{_includedir}/LayerShellQt
%{_libdir}/cmake/LayerShellQt

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
