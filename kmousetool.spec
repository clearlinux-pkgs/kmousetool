#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmousetool
Version  : 19.08.2
Release  : 13
URL      : https://download.kde.org/stable/applications/19.08.2/src/kmousetool-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/kmousetool-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/kmousetool-19.08.2.tar.xz.sig
Summary  : Clicks the mouse for you, reducing the effects of RSI
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kmousetool-bin = %{version}-%{release}
Requires: kmousetool-data = %{version}-%{release}
Requires: kmousetool-license = %{version}-%{release}
Requires: kmousetool-locales = %{version}-%{release}
Requires: kmousetool-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : phonon-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kmousetool-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570749127
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570749127
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmousetool
cp COPYING %{buildroot}/usr/share/package-licenses/kmousetool/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kmousetool/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang kmousetool

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/package-licenses/kmousetool/COPYING
/usr/share/package-licenses/kmousetool/COPYING.DOC

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

