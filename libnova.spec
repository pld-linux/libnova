Summary:	General purpose astronomy & astrodynamics library
Summary(pl.UTF-8):	Biblioteka astronomiczna i astrodynamiczna ogólnego przeznaczenia
Name:		libnova
Version:	0.14.0
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libnova/%{name}-%{version}.tar.gz
# Source0-md5:	e81a00efedfa3043cd6018383e8a0438
URL:		http://libnova.sourceforge.net/
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
%setup -q

%build
%configure
%{__make} \
       CFLAGS="%{rpmcflags}" \
       LDFLAGS="%{rpmldflags}"

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
%attr(755,root,root) %{_libdir}/libnova-0.14.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnova-0.14.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnova.so
%{_libdir}/libnova.la
%{_includedir}/libnova

%files static
%defattr(644,root,root,755)
%{_libdir}/libnova.a
