Summary:	Tcl interface for PostgreSQL
Summary(es):	Bibliotecas y shell Tcl para acceder un servidor PostgreSQL
Summary(pl):	Interfejs Tcl dla PostgreSQL
Summary(pt_BR):	Bibliotecas e shell para programas em Tcl acessarem o servidor PostgreSQL
Summary(ru):	Библиотеки для доступа к PostgreSQL из Tcl
Summary(uk):	Б╕бл╕отеки для доступу до PostgreSQL з Tcl
Summary(zh_CN):	р╩╦Ж Tcl ©Б╨м PostgreSQL ╣д PL/Tcl ╠ЮЁлсОят
Name:		tcl-libpgtcl
Version:	1.4
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	ftp://gborg.postgresql.org/pub/pgtcl/stable/libpgtcl-%{version}.tar.gz
# Source0-md5:	6666ab358f2b8ae822dafff29c7dd1d7
URL:		http://gborg.postgresql.org/project/pgtcl/projdisplay.php
BuildRequires:	postgresql-devel
BuildRequires:	tcl-devel >= 8
Obsoletes:	postgresql-tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl interface for PostgreSQL.

%description -l es
Bibliotecas y shell Tcl para acceder un servidor PostgreSQL.

%description -l pl
Interfejs Tcl dla PostgreSQL.

%description -l pt_BR
Bibliotecas e shell para programas em Tcl acessarem o servidor
PostgreSQL.

%description -l ru
libpgtcl - API для доступа к базе данных PostgreSQL из языка Tcl.

%description -l uk
libpgtcl - API для доступу до бази даних PostgreSQL з мови Tcl.

%package devel
Summary:	Development part of Tcl interface for PostgreSQL
Summary(pl):	CzЙ╤Ф dla programistСw interfejsu Tcl dla PostgreSQL
Summary(ru):	Хедеры и библиотеки для разработок с использованием libpgtcl (Tcl интерфейс для PostgreSQL)
Summary(uk):	Хедери та б╕бл╕отеки для розробок з використанням libpgtcl (Tcl-╕нтерфейс для PostgreSQL)
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql-devel
Obsoletes:	postgresql-tcl-devel
Obsoletes:	postgresql-tcl-static

%description devel
Development part of Tcl interface for PostgreSQL.

%description devel -l pl
CzЙ╤Ф interfejsu Tcl dla PostgreSQL przeznaczona dla programistСw.

%description devel -l ru
Это пакет разработчика для программирования с libpgtcl. Он включает
хедеры и библиотеки для использования в программах, которые используют
код или API libtcl (Tcl интерфейс для PostgreSQL).

%description devel -l uk
Це пакет програм╕ста для програмування з libpgtcl. В╕н м╕стить хедери
та б╕бл╕отеки для використання в програмах, як╕ використовують код або
API libtcl (Tcl-╕нтерфейсу для PostgreSQL).

%prep
%setup -q -n libpgtcl

find . -type d -name CVS | xargs rm -rf 

# workaround for broken make install
touch doc/fake.n

%build
%configure2_13

%{__make} \
	CFLAGS_OPTIMIZE="%{rpmcflags} -D__NO_STRING_INLINES -D__NO_MATH_INLINES"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.async TODO
%dir %{_libdir}/pgtcl1.4
%attr(755,root,root) %{_libdir}/pgtcl1.4/libpgtcl1.4.so
%{_libdir}/pgtcl1.4/pkgIndex.tcl

%files devel
%defattr(644,root,root,755)
%doc doc/{NEW-COMMANDS,PGTCL-NOTES,libpgtcl.pdf} doc/html
%{_includedir}/libpgtcl.h
