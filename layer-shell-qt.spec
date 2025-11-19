%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define major 6
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		layer-shell-qt
Version:	6.5.3
Release:	%{?git:0.%{git}.}1
Summary:	Qt component to allow applications to make use of the Wayland wl-layer-shell protocol
Group:		System/Libraries
License:	GPLv2
URL:		https://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/layer-shell-qt/-/archive/%{gitbranch}/layer-shell-qt-%{gitbranchd}.tar.bz2#/layer-shell-qt-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/layer-shell-qt-%{version}.tar.xz
%endif
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(xkbcommon)
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2025-04-27
%rename plasma6-layer-shell-qt

%description
Qt component to allow applications to make use of the Wayland wl-layer-shell protocol

%files
%dir %{_qtdir}/plugins/wayland-shell-integration
%{_qtdir}/plugins/wayland-shell-integration/liblayer-shell.so
# No need to split this into a package of its own, the library is useless
# without the Qt plugin
%{_libdir}/libLayerShellQtInterface.so.*
# Splitting the QML bits may make sense, but they're probably very common
%{_qtdir}/qml/org/kde/layershell

#------------------------------------------------------------------------------
%define olddevname %mklibname LayerShellQtInterface6 -d
%define devname %mklibname LayerShellQtInterface -d

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
# Renamed after 6.0 2025-04-27
%rename %{olddevname}

%description -n %{devname}
Qt component to allow applications to make use of the Wayland wl-layer-shell protocol

%files -n %{devname}
%{_libdir}/libLayerShellQtInterface.so
%{_includedir}/LayerShellQt
%{_libdir}/cmake/LayerShellQt
