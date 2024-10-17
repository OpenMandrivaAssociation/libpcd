%define major	2
%define libname %mklibname pcd

Summary:	Library for decoding PhotoCD images
Name:		libpcd
Version:	1.0.3
Release:	1
License:	GPL
Group:		Graphics
URL:		https://linux.bytesex.org/fbida/libpcd.html
Source:		https://git.kraxel.org/cgit/libpcd/snapshot/libpcd-%{version}-1.tar.gz

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
%autosetup -p1 -n %{name}-%{version}-1

%build
export CFLAGS="%optflags"
%make_build prefix=%{_prefix} libdir=%{_libdir}

%install
%make_install prefix=%{_prefix} libdir=%{buildroot}%{_libdir}

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
