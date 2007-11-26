%define	version	1.0.1
%define release	3mdk

%define major	2
%define libname %mklibname pcd %{major}

Summary:	Library for decoding PhotoCD images
Name:		libpcd
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphics
URL:		http://linux.bytesex.org/fbida/libpcd.html
Source:		http://dl.bytesex.org/releases/%{name}/%{name}_%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{name} is a tiny library for decoding PhotoCD images. It used to come
bundled with xpcd, but software maintainer decided to release the library
separately after declaring xpcd obsolete.


%package	-n %{libname}
Summary:	Library for decoding PhotoCD images
Group:		Graphics
Provides:	%{name} = %{version}-%{release}

%description	-n %{libname}
%{name} is a tiny library for decoding PhotoCD images. It used to come
bundled with xpcd, but software maintainer decided to release the library
separately after declaring xpcd obsolete.

%package	-n %{libname}-devel
Summary:	Development related files of %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description	-n %{libname}-devel
%{name} is a tiny library for decoding PhotoCD images. It used to come
bundled with xpcd, but software maintainer decided to release the library
separately after declaring xpcd obsolete.

This package contains all files you need to compile applications/libraries
that has Photo CD image support.

%prep
%setup -q

%build
export CFLAGS="%optflags"
%make

%install
rm -rf %{buildroot}
%makeinstall

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc pcd.css pcd.html
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a

