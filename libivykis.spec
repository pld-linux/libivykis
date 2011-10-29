Summary:	Wrapper over various OS'es implementation of I/O readiness notification facilities
Name:		libivykis
Version:	0.23
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libivykis/ivykis-%{version}.tar.gz
# Source0-md5:	60ae0155ba4cb37751ff0c2ee92f68a1
URL:		http://libivykis.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libivykis is a thin wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and is
mainly intended for writing portable high-performance network servers.

%package devel
Summary:	Header files for libivykis
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libivykis
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libivykis.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libivykis.

%package static
Summary:	Static libivykis library
Summary(pl.UTF-8):	Biblioteka statyczna libivykis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libivykis library.

%description static -l pl.UTF-8
Biblioteka statyczna libivykis.

%prep
%setup -q -n ivykis-%{version}

%build
%{__libtoolize}
%{__automake}
%{__aclocal}
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
#%attr(755,root,root) %{_libdir}/libevtlog.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libevtlog.so.0

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libevtlog.so
#%{_libdir}/libevtlog.la
#%{_includedir}/ivykis
#%{_pkgconfigdir}/ivykis.pc

%files static
%defattr(644,root,root,755)
#%{_libdir}/libevtlog.a
