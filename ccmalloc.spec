Name:		ccmalloc
Version:	0.3.2
%define fnversion %(echo %{version} | tr . -)
Release:	1
Summary:	C/C++ memory debugging and profiling library
License:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source0:	http://www.inf.ethz.ch/personal/biere/projects/ccmalloc/%{name}-%{fnversion}.tar.gz
URL:		http://www.inf.ethz.ch/personal/biere/projects/ccmalloc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ccmalloc detects memory leaks, multiple deallocations, over-writes,
under-writes and access of deallocated data in C and C++ code, all
without source recompile.

It also displays statistics on allocation and deallocation.

%prep
%setup -q -n %{name}-%{fnversion}

%build
./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_libdir}
install lib/libccmalloc.a ${RPM_BUILD_ROOT}%{_libdir}
install obj/ccmalloc.o	  ${RPM_BUILD_ROOT}%{_libdir}
gzip -9nf BUGS FEATURES INSTALL NEWS README TODO USAGE

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%{_libdir}
%doc {BUGS,FEATURES,INSTALL,NEWS,README,TODO,USAGE}.gz
%doc ccmalloc.cfg
