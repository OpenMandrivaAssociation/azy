#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/PROTO/azy azy; \
#cd azy; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf azy-$PKG_VERSION.tar.xz azy/ --exclude .svn --exclude .*ignore

%define svndate 20120103
%define svnrev  66485

%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Lazy RPC client/server library
Name:		azy
Version:	1.0.0.%{svnrev}
Release:	0.%{svndate}.1
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.tar.xz
BuildRequires:  byacc
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(eina)

%description
Azy is a full rewrite of libzxr, itself a modification of libxr. It
is meant for implementing rpc clients and servers in a simple manner.

%package -n %{libname}
Summary:    Libraries for the edje package
Group:      System/Libraries

%description -n %{libname}
Azy is a full rewrite of libzxr, itself a modification of libxr. It 
is meant for implementing rpc clients and servers in a simple manner.

Libraries for azy.

%package -n %{develname}
Summary:    Enlightenment azy headers and development libraries
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
Azy development headers and libraries.
%prep
%setup -qn %{name}


%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -fr %{buildroot}
%makeinstall

%files -n %{libname}
%{_libdir}/libazy.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING README
%{_bindir}/azy_parser
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

