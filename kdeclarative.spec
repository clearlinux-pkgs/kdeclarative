#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdeclarative
Version  : 5.85.0
Release  : 38
URL      : https://download.kde.org/stable/frameworks/5.85/kdeclarative-5.85.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.85/kdeclarative-5.85.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.85/kdeclarative-5.85.0.tar.xz.sig
Summary  : Provides integration of QML and KDE Frameworks
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kdeclarative-bin = %{version}-%{release}
Requires: kdeclarative-lib = %{version}-%{release}
Requires: kdeclarative-license = %{version}-%{release}
Requires: kdeclarative-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : kpackage-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : libepoxy-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

%description
This import contains KDE extras that are visually similar to Qt Quick Controls.

%package bin
Summary: bin components for the kdeclarative package.
Group: Binaries
Requires: kdeclarative-license = %{version}-%{release}

%description bin
bin components for the kdeclarative package.


%package dev
Summary: dev components for the kdeclarative package.
Group: Development
Requires: kdeclarative-lib = %{version}-%{release}
Requires: kdeclarative-bin = %{version}-%{release}
Provides: kdeclarative-devel = %{version}-%{release}
Requires: kdeclarative = %{version}-%{release}

%description dev
dev components for the kdeclarative package.


%package lib
Summary: lib components for the kdeclarative package.
Group: Libraries
Requires: kdeclarative-license = %{version}-%{release}

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
%setup -q -n kdeclarative-5.85.0
cd %{_builddir}/kdeclarative-5.85.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630903152
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1630903152
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdeclarative
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdeclarative/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdeclarative/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdeclarative/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdeclarative/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdeclarative/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kdeclarative/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdeclarative/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdeclarative/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdeclarative/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdeclarative/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdeclarative/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kdeclarative-5.85.0/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kdeclarative/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
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
/usr/include/KF5/KDeclarative/KQuickAddons/ManagedConfigModule
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
/usr/include/KF5/KDeclarative/kquickaddons/managedconfigmodule.h
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
/usr/lib64/libKF5CalendarEvents.so.5.85.0
/usr/lib64/libKF5Declarative.so.5
/usr/lib64/libKF5Declarative.so.5.85.0
/usr/lib64/libKF5QuickAddons.so.5
/usr/lib64/libKF5QuickAddons.so.5.85.0
/usr/lib64/qt5/qml/org/kde/draganddrop/libdraganddropplugin.so
/usr/lib64/qt5/qml/org/kde/draganddrop/qmldir
/usr/lib64/qt5/qml/org/kde/graphicaleffects/Lanczos.qml
/usr/lib64/qt5/qml/org/kde/graphicaleffects/lanczos2sharp.frag
/usr/lib64/qt5/qml/org/kde/graphicaleffects/lanczos2sharp_core.frag
/usr/lib64/qt5/qml/org/kde/graphicaleffects/preserveaspect.vert
/usr/lib64/qt5/qml/org/kde/graphicaleffects/preserveaspect_core.vert
/usr/lib64/qt5/qml/org/kde/graphicaleffects/qmldir
/usr/lib64/qt5/qml/org/kde/kcm/AbstractKCM.qml
/usr/lib64/qt5/qml/org/kde/kcm/ContextualHelpButton.qml
/usr/lib64/qt5/qml/org/kde/kcm/GridDelegate.qml
/usr/lib64/qt5/qml/org/kde/kcm/GridView.qml
/usr/lib64/qt5/qml/org/kde/kcm/GridViewKCM.qml
/usr/lib64/qt5/qml/org/kde/kcm/ScrollView.qml
/usr/lib64/qt5/qml/org/kde/kcm/ScrollViewKCM.qml
/usr/lib64/qt5/qml/org/kde/kcm/SettingHighlighter.qml
/usr/lib64/qt5/qml/org/kde/kcm/SettingStateBinding.qml
/usr/lib64/qt5/qml/org/kde/kcm/SimpleKCM.qml
/usr/lib64/qt5/qml/org/kde/kcm/libkcmcontrolsplugin.so
/usr/lib64/qt5/qml/org/kde/kcm/private/GridViewInternal.qml
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdeclarative/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdeclarative/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdeclarative/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdeclarative/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kdeclarative/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kdeclarative/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdeclarative/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kdeclarative/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kdeclarative/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kdeclarative/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kdeclarative5.lang
%defattr(-,root,root,-)

