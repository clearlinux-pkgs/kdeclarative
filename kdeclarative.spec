#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdeclarative
Version  : 5.48.0
Release  : 1
URL      : https://download.kde.org/stable/frameworks/5.48/kdeclarative-5.48.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.48/kdeclarative-5.48.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.48/kdeclarative-5.48.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kdeclarative-bin
Requires: kdeclarative-lib
Requires: kdeclarative-license
Requires: kdeclarative-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kbookmarks-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kpackage-dev
BuildRequires : kservice-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : solid-dev

%description
This import contains KDE extras that are visually similar to Qt Quick Controls.

%package bin
Summary: bin components for the kdeclarative package.
Group: Binaries
Requires: kdeclarative-license

%description bin
bin components for the kdeclarative package.


%package dev
Summary: dev components for the kdeclarative package.
Group: Development
Requires: kdeclarative-lib
Requires: kdeclarative-bin
Provides: kdeclarative-devel

%description dev
dev components for the kdeclarative package.


%package lib
Summary: lib components for the kdeclarative package.
Group: Libraries
Requires: kdeclarative-license

%description lib
lib components for the kdeclarative package.


%package license
Summary: license components for the kdeclarative package.
Group: Default

%description license
license components for the kdeclarative package.


%package locales
Summary: locales components for the kdeclarative package.
Group: Default

%description locales
locales components for the kdeclarative package.


%prep
%setup -q -n kdeclarative-5.48.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532185360
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1532185360
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kdeclarative
cp COPYING.LIB %{buildroot}/usr/share/doc/kdeclarative/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kdeclarative5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kpackagelauncherqml

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KDeclarative/CalendarEvents/CalendarEventsPlugin
/usr/include/KF5/KDeclarative/KDeclarative/ConfigPropertyMap
/usr/include/KF5/KDeclarative/KDeclarative/KDeclarative
/usr/include/KF5/KDeclarative/KDeclarative/QmlObject
/usr/include/KF5/KDeclarative/KDeclarative/QmlObjectSharedEngine
/usr/include/KF5/KDeclarative/KQuickAddons/ConfigModule
/usr/include/KF5/KDeclarative/KQuickAddons/ImageTexturesCache
/usr/include/KF5/KDeclarative/KQuickAddons/ManagedTextureNode
/usr/include/KF5/KDeclarative/KQuickAddons/QtQuickSettings
/usr/include/KF5/KDeclarative/KQuickAddons/QuickViewSharedEngine
/usr/include/KF5/KDeclarative/QuickAddons/ImageTexturesCache
/usr/include/KF5/KDeclarative/QuickAddons/ManagedTextureNode
/usr/include/KF5/KDeclarative/calendarevents/calendarevents_export.h
/usr/include/KF5/KDeclarative/calendarevents/calendareventsplugin.h
/usr/include/KF5/KDeclarative/kdeclarative/configpropertymap.h
/usr/include/KF5/KDeclarative/kdeclarative/kdeclarative.h
/usr/include/KF5/KDeclarative/kdeclarative/kdeclarative_export.h
/usr/include/KF5/KDeclarative/kdeclarative/qmlobject.h
/usr/include/KF5/KDeclarative/kdeclarative/qmlobjectsharedengine.h
/usr/include/KF5/KDeclarative/kquickaddons/configmodule.h
/usr/include/KF5/KDeclarative/kquickaddons/imagetexturescache.h
/usr/include/KF5/KDeclarative/kquickaddons/managedtexturenode.h
/usr/include/KF5/KDeclarative/kquickaddons/qtquicksettings.h
/usr/include/KF5/KDeclarative/kquickaddons/quickaddons_export.h
/usr/include/KF5/KDeclarative/kquickaddons/quickviewsharedengine.h
/usr/include/KF5/KDeclarative/quickaddons/imagetexturescache.h
/usr/include/KF5/KDeclarative/quickaddons/managedtexturenode.h
/usr/include/KF5/KDeclarative/quickaddons/quickaddons_export.h
/usr/include/KF5/kdeclarative_version.h
/usr/lib64/cmake/KF5Declarative/KF5DeclarativeConfig.cmake
/usr/lib64/cmake/KF5Declarative/KF5DeclarativeConfigVersion.cmake
/usr/lib64/cmake/KF5Declarative/KF5DeclarativeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Declarative/KF5DeclarativeTargets.cmake
/usr/lib64/libKF5CalendarEvents.so
/usr/lib64/libKF5Declarative.so
/usr/lib64/libKF5QuickAddons.so
/usr/lib64/qt5/mkspecs/modules/qt_KDeclarative.pri
/usr/lib64/qt5/mkspecs/modules/qt_QuickAddons.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5CalendarEvents.so.5
/usr/lib64/libKF5CalendarEvents.so.5.48.0
/usr/lib64/libKF5Declarative.so.5
/usr/lib64/libKF5Declarative.so.5.48.0
/usr/lib64/libKF5QuickAddons.so.5
/usr/lib64/libKF5QuickAddons.so.5.48.0
/usr/lib64/qt5/qml/org/kde/draganddrop/libdraganddropplugin.so
/usr/lib64/qt5/qml/org/kde/draganddrop/qmldir
/usr/lib64/qt5/qml/org/kde/kcm/GridDelegate.qml
/usr/lib64/qt5/qml/org/kde/kcm/GridView.qml
/usr/lib64/qt5/qml/org/kde/kcm/GridViewKCM.qml
/usr/lib64/qt5/qml/org/kde/kcm/ScrollView.qml
/usr/lib64/qt5/qml/org/kde/kcm/ScrollViewKCM.qml
/usr/lib64/qt5/qml/org/kde/kcm/SimpleKCM.qml
/usr/lib64/qt5/qml/org/kde/kcm/libkcmcontrolsplugin.so
/usr/lib64/qt5/qml/org/kde/kcm/qmldir
/usr/lib64/qt5/qml/org/kde/kconfig/libkconfigplugin.so
/usr/lib64/qt5/qml/org/kde/kconfig/qmldir
/usr/lib64/qt5/qml/org/kde/kcoreaddons/libkcoreaddonsplugin.so
/usr/lib64/qt5/qml/org/kde/kcoreaddons/qmldir
/usr/lib64/qt5/qml/org/kde/kio/libkio.so
/usr/lib64/qt5/qml/org/kde/kio/qmldir
/usr/lib64/qt5/qml/org/kde/kquickcontrols/ColorButton.qml
/usr/lib64/qt5/qml/org/kde/kquickcontrols/KeySequenceItem.qml
/usr/lib64/qt5/qml/org/kde/kquickcontrols/qmldir
/usr/lib64/qt5/qml/org/kde/kquickcontrolsaddons/libkquickcontrolsaddonsplugin.so
/usr/lib64/qt5/qml/org/kde/kquickcontrolsaddons/qmldir
/usr/lib64/qt5/qml/org/kde/kwindowsystem/libkwindowsystem.so
/usr/lib64/qt5/qml/org/kde/kwindowsystem/qmldir
/usr/lib64/qt5/qml/org/kde/private/kquickcontrols/libkquickcontrolsprivateplugin.so
/usr/lib64/qt5/qml/org/kde/private/kquickcontrols/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/kdeclarative/COPYING.LIB

%files locales -f kdeclarative5.lang
%defattr(-,root,root,-)

