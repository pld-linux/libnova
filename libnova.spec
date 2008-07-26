Summary:	Libnova is a general purpose astronomy & astrodynamics library
Name:		libnova
Version:	0.12.2
Release:	1
License:	LGPL
Group:		Libraries
URL:		http://libnova.sourceforge.net/
Source0:	http://dl.sourceforge.net/libnova/%{name}-%{version}.tar.gz
# Source0-md5:	093e93e812cf97269b7ee338dae2e1c5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libnova is a general purpose, double precision, celestial mechanics,
astrometry and astrodynamics library.

%package devel
Summary:	Header files and static libraries from libnova
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and includes files for developing programs based on libnova.

%prep
%setup -q

%build
%configure
%{__make} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# get rid of *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/libnova.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%attr(755,root,root) %{_bindir}/libnovaconfig
%attr(755,root,root) %{_libdir}/libnova-0.12.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libnova
%{_libdir}/libnova.a
%{_libdir}/libnova.so
