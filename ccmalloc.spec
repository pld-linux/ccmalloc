Summary:	C/C++ memory debugging and profiling library
Summary(pl):	Biblioteka do debuggowania i profilowania obs³ugi pamiêci w C/C++
Name:		ccmalloc
Version:	0.3.4
%define fnversion %(echo %{version} | tr . -)
Release:	1
License:	GPL
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source0:	http://www.inf.ethz.ch/personal/biere/projects/ccmalloc/%{name}-%{fnversion}.tar.gz
URL:		http://www.inf.ethz.ch/personal/biere/projects/ccmalloc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ccmalloc detects memory leaks, multiple deallocations, over-writes,
under-writes and access of deallocated data in C and C++ code, all
without source recompile.

It also displays statistics on allocation and deallocation.

%description -l pl
ccmalloc wykrywa wycieki pamiêci, wielokrotne zwalnianie, zapisy
poni¿ej i powy¿ej zaalokowanego obszaru oraz dostêp do zwolnionego
obszaru pamiêci w programach w C i C++ - bez rekompilacji.

Wy¶wietla tak¿e statystyki alokacji i dealokacji.

%prep
%setup -q -n %{name}-%{fnversion}

%build
./configure --prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_libdir}

install lib/libccmalloc.a ${RPM_BUILD_ROOT}%{_libdir}
install obj/ccmalloc*.o	  ${RPM_BUILD_ROOT}%{_libdir}

gzip -9nf BUGS FEATURES NEWS README TODO USAGE

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%{_libdir}/*
%doc {BUGS,FEATURES,NEWS,README,TODO,USAGE}.gz
%doc ccmalloc.cfg
