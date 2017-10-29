Summary:	Wrapper over various OS'es implementation of I/O readiness notification facilities
Summary(pl.UTF-8):	Obudowanie implementacji różnych OS-ów powiadamiania o dostępności we/wy
Name:		libivykis
Version:	0.42.2
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libivykis/ivykis-%{version}.tar.gz
# Source0-md5:	392cc7acf46fd1b8c69d430b0e9d81b1
URL:		http://libivykis.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libivykis is a thin wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and is
mainly intended for writing portable high-performance network servers.

%description -l pl.UTF-8
libivykis to małe obudowanie obecnych w różnych systemach operacyjnych
implementacji powiadamiania o dostępności wejścia/wyjścia (takich jak
poll(2), kqueue(2)). Biblioteka jest przeznaczona do pisania
przenośnych, wysoko wydajnych serwerów sieciowych.

%package devel
Summary:	Header files for libivykis libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libivykis
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libivykis libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libivykis.

%package static
Summary:	Static libivykis libraries
Summary(pl.UTF-8):	Biblioteki statyczne libivykis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libivykis libraries.

%description static -l pl.UTF-8
Biblioteki statyczne libivykis.

%prep
%setup -q -n ivykis-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS DEDICATION
%attr(755,root,root) %{_libdir}/libivykis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libivykis.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libivykis.so
%{_libdir}/libivykis.la
%{_includedir}/iv*.h
%{_pkgconfigdir}/ivykis.pc
%{_mandir}/man3/IV_*.3*
%{_mandir}/man3/iv_*.3*
%{_mandir}/man3/ivykis.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libivykis.a
