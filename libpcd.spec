%define	version	1.0.1
%define release	 8

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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2011.0
+ Revision: 620214
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2010.0
+ Revision: 429826
- rebuild

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2009.0
+ Revision: 250404
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2008.1
+ Revision: 128984
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import libpcd


* Fri Jan 21 2005 Abel Cheung <deaddog@mandrake.org> 1.0.1-3mdk
- Fix rpmlint warning
- New URL

* Fri Jan 21 2005 Abel Cheung <deaddog@mandrake.org> 1.0.1-2mdk
- rebuild

* Tue Dec 02 2003 Abel Cheung <deaddog@deaddog.org> 1.0.1-1mdk
- First Mandrake package
