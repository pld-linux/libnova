#
# Conditional build:
%bcond_with	avx	# AVX instructions

Summary:	General purpose astronomy & astrodynamics library
Summary(pl.UTF-8):	Biblioteka astronomiczna i astrodynamiczna ogólnego przeznaczenia
Name:		libnova
Version:	0.16
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://gitlab.com/libnova/libnova/-/tags
Source0:	https://gitlab.com/libnova/libnova/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	85dafbc9ec042e483d2f68849feb2d9a
Patch0:		%{name}-opt.patch
URL:		https://gitlab.com/libnova/libnova
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	libtool >= 2:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libnova is a general purpose, double precision, celestial mechanics,
astrometry and astrodynamics library.

%description -l pl.UTF-8
Libnova to ogólnego przeznaczenia biblioteka funkcji podwójnej
precyzji z dziedziny mechaniki ciał niebieskich, astrometrii i
astrodynamiki.

%package devel
Summary:	Header files for libnova
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnova
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnova.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnova.

%package static
Summary:	Static libnova library
Summary(pl.UTF-8):	Statyczna biblioteka libnova
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnova library.

%description static -l pl.UTF-8
Statyczna biblioteka libnova.

%prep
%setup -q -n %{name}-v%{version}
%patch -P0 -p1
echo %{version} > .tarball-version

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_avx:--enable-avx}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/libnovaconfig
%{_libdir}/libnova-0.16.so.*.*.*
%ghost %{_libdir}/libnova-0.16.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libnova.so
%{_libdir}/libnova.la
%{_includedir}/libnova

%files static
%defattr(644,root,root,755)
%{_libdir}/libnova.a
