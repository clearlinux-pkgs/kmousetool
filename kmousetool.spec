#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmousetool
Version  : 24.08.0
Release  : 73
URL      : https://download.kde.org/stable/release-service/24.08.0/src/kmousetool-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/kmousetool-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/kmousetool-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kmousetool-bin = %{version}-%{release}
Requires: kmousetool-data = %{version}-%{release}
Requires: kmousetool-license = %{version}-%{release}
Requires: kmousetool-locales = %{version}-%{release}
Requires: kmousetool-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
MouseTool is a program that clicks the mouse for you.
I designed it to help relieve the pain that clicking mouse buttons can cause.

%package bin
Summary: bin components for the kmousetool package.
Group: Binaries
Requires: kmousetool-data = %{version}-%{release}
Requires: kmousetool-license = %{version}-%{release}

%description bin
bin components for the kmousetool package.


%package data
Summary: data components for the kmousetool package.
Group: Data

%description data
data components for the kmousetool package.


%package doc
Summary: doc components for the kmousetool package.
Group: Documentation
Requires: kmousetool-man = %{version}-%{release}

%description doc
doc components for the kmousetool package.


%package license
Summary: license components for the kmousetool package.
Group: Default

%description license
license components for the kmousetool package.


%package locales
Summary: locales components for the kmousetool package.
Group: Default

%description locales
locales components for the kmousetool package.


%package man
Summary: man components for the kmousetool package.
Group: Default

%description man
man components for the kmousetool package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kmousetool-24.08.0
cd %{_builddir}/kmousetool-24.08.0
pushd ..
cp -a kmousetool-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724519600
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
export SOURCE_DATE_EPOCH=1724519600
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmousetool
cp %{_builddir}/kmousetool-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmousetool/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kmousetool-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kmousetool/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc || :
cp %{_builddir}/kmousetool-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmousetool/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
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
%find_lang kmousetool
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kmousetool
/usr/bin/kmousetool

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kmousetool.desktop
/usr/share/icons/hicolor/16x16/actions/kmousetool_off.png
/usr/share/icons/hicolor/16x16/actions/kmousetool_on.png
/usr/share/icons/hicolor/16x16/apps/kmousetool.png
/usr/share/icons/hicolor/32x32/actions/kmousetool_off.png
/usr/share/icons/hicolor/32x32/actions/kmousetool_on.png
/usr/share/icons/hicolor/32x32/apps/kmousetool.png
/usr/share/kmousetool/sounds/mousetool_tap.wav
/usr/share/metainfo/org.kde.kmousetool.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmousetool/index.cache.bz2
/usr/share/doc/HTML/ca/kmousetool/index.docbook
/usr/share/doc/HTML/de/kmousetool/index.cache.bz2
/usr/share/doc/HTML/de/kmousetool/index.docbook
/usr/share/doc/HTML/en/kmousetool/index.cache.bz2
/usr/share/doc/HTML/en/kmousetool/index.docbook
/usr/share/doc/HTML/es/kmousetool/index.cache.bz2
/usr/share/doc/HTML/es/kmousetool/index.docbook
/usr/share/doc/HTML/fr/kmousetool/index.cache.bz2
/usr/share/doc/HTML/fr/kmousetool/index.docbook
/usr/share/doc/HTML/it/kmousetool/index.cache.bz2
/usr/share/doc/HTML/it/kmousetool/index.docbook
/usr/share/doc/HTML/nl/kmousetool/index.cache.bz2
/usr/share/doc/HTML/nl/kmousetool/index.docbook
/usr/share/doc/HTML/pt/kmousetool/index.cache.bz2
/usr/share/doc/HTML/pt/kmousetool/index.docbook
/usr/share/doc/HTML/pt_BR/kmousetool/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmousetool/index.docbook
/usr/share/doc/HTML/ru/kmousetool/index.cache.bz2
/usr/share/doc/HTML/ru/kmousetool/index.docbook
/usr/share/doc/HTML/sv/kmousetool/index.cache.bz2
/usr/share/doc/HTML/sv/kmousetool/index.docbook
/usr/share/doc/HTML/uk/kmousetool/index.cache.bz2
/usr/share/doc/HTML/uk/kmousetool/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmousetool/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kmousetool/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kmousetool/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kmousetool.1
/usr/share/man/de/man1/kmousetool.1
/usr/share/man/es/man1/kmousetool.1
/usr/share/man/et/man1/kmousetool.1
/usr/share/man/fr/man1/kmousetool.1
/usr/share/man/it/man1/kmousetool.1
/usr/share/man/man1/kmousetool.1
/usr/share/man/nl/man1/kmousetool.1
/usr/share/man/pt/man1/kmousetool.1
/usr/share/man/pt_BR/man1/kmousetool.1
/usr/share/man/sv/man1/kmousetool.1
/usr/share/man/uk/man1/kmousetool.1

%files locales -f kmousetool.lang
%defattr(-,root,root,-)

