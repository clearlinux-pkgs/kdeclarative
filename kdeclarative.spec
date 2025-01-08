#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kdeclarative
Version  : 6.9.0
Release  : 88
URL      : https://download.kde.org/stable/frameworks/6.9/kdeclarative-6.9.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.9/kdeclarative-6.9.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.9/kdeclarative-6.9.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Provides integration of QML and KDE Frameworks
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT
Requires: kdeclarative-lib = %{version}-%{release}
Requires: kdeclarative-license = %{version}-%{release}
Requires: kdeclarative-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kglobalaccel-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This import contains KDE extras that are visually similar to Qt Quick Controls.

%package dev
Summary: dev components for the kdeclarative package.
Group: Development
Requires: kdeclarative-lib = %{version}-%{release}
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kdeclarative-6.9.0
cd %{_builddir}/kdeclarative-6.9.0
pushd ..
cp -a kdeclarative-6.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735245659
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735245659
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdeclarative
cp %{_builddir}/kdeclarative-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdeclarative/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdeclarative-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdeclarative/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kdeclarative-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdeclarative/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kdeclarative-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdeclarative/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kdeclarative-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kdeclarative/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kdeclarative-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdeclarative/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdeclarative-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdeclarative/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdeclarative-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kdeclarative/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kdeclarative6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KDeclarative/CalendarEvents/CalendarEventsPlugin
/usr/include/KF6/KDeclarative/calendarevents/calendarevents_export.h
/usr/include/KF6/KDeclarative/calendarevents/calendareventsplugin.h
/usr/include/KF6/KDeclarative/kdeclarative_version.h
/usr/lib64/cmake/KF6Declarative/KF6DeclarativeConfig.cmake
/usr/lib64/cmake/KF6Declarative/KF6DeclarativeConfigVersion.cmake
/usr/lib64/cmake/KF6Declarative/KF6DeclarativeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Declarative/KF6DeclarativeTargets.cmake
/usr/lib64/libKF6CalendarEvents.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6CalendarEvents.so.6.9.0
/V3/usr/lib64/qt6/qml/org/kde/draganddrop/libdraganddropplugin.so
/V3/usr/lib64/qt6/qml/org/kde/graphicaleffects/libgraphicaleffects.so
/V3/usr/lib64/qt6/qml/org/kde/kquickcontrolsaddons/libkquickcontrolsaddonsplugin.so
/V3/usr/lib64/qt6/qml/org/kde/private/kquickcontrols/libkquickcontrolsprivateplugin.so
/usr/lib64/libKF6CalendarEvents.so.6
/usr/lib64/libKF6CalendarEvents.so.6.9.0
/usr/lib64/qt6/qml/org/kde/draganddrop/draganddropplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/draganddrop/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/draganddrop/libdraganddropplugin.so
/usr/lib64/qt6/qml/org/kde/draganddrop/qmldir
/usr/lib64/qt6/qml/org/kde/graphicaleffects/BadgeEffect.qml
/usr/lib64/qt6/qml/org/kde/graphicaleffects/Lanczos.qml
/usr/lib64/qt6/qml/org/kde/graphicaleffects/graphicaleffects.qmltypes
/usr/lib64/qt6/qml/org/kde/graphicaleffects/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/graphicaleffects/libgraphicaleffects.so
/usr/lib64/qt6/qml/org/kde/graphicaleffects/qmldir
/usr/lib64/qt6/qml/org/kde/kquickcontrols/ColorButton.qml
/usr/lib64/qt6/qml/org/kde/kquickcontrols/KeySequenceItem.qml
/usr/lib64/qt6/qml/org/kde/kquickcontrols/qmldir
/usr/lib64/qt6/qml/org/kde/kquickcontrolsaddons/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kquickcontrolsaddons/kquickcontrolsaddonsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kquickcontrolsaddons/libkquickcontrolsaddonsplugin.so
/usr/lib64/qt6/qml/org/kde/kquickcontrolsaddons/qmldir
/usr/lib64/qt6/qml/org/kde/private/kquickcontrols/libkquickcontrolsprivateplugin.so
/usr/lib64/qt6/qml/org/kde/private/kquickcontrols/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdeclarative/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdeclarative/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdeclarative/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kdeclarative/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kdeclarative/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kdeclarative/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdeclarative/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3

%files locales -f kdeclarative6.lang
%defattr(-,root,root,-)

