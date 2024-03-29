Summary:	Tcl interface for PostgreSQL
Summary(es.UTF-8):	Bibliotecas y shell Tcl para acceder un servidor PostgreSQL
Summary(pl.UTF-8):	Interfejs Tcl dla PostgreSQL
Summary(pt_BR.UTF-8):	Bibliotecas e shell para programas em Tcl acessarem o servidor PostgreSQL
Summary(ru.UTF-8):	Библиотеки для доступа к PostgreSQL из Tcl
Summary(uk.UTF-8):	Бібліотеки для доступу до PostgreSQL з Tcl
Summary(zh_CN.UTF-8):	一个 Tcl 库和 PostgreSQL 的 PL/Tcl 编程语言
Name:		tcl-libpgtcl
Version:	1.5
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://pgfoundry.org/frs/download.php/338/pgtcl%{version}.tar.gz
# Source0-md5:	6eed1c338fc3bb7a844797c92b79b936
URL:		http://pgfoundry.org/projects/pgtcl/
BuildRequires:	postgresql-devel
BuildRequires:	tcl-devel >= 8
Provides:	tcl(Pgtcl)
Obsoletes:	postgresql-tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl interface for PostgreSQL.

%description -l es.UTF-8
Bibliotecas y shell Tcl para acceder un servidor PostgreSQL.

%description -l pl.UTF-8
Interfejs Tcl dla PostgreSQL.

%description -l pt_BR.UTF-8
Bibliotecas e shell para programas em Tcl acessarem o servidor
PostgreSQL.

%description -l ru.UTF-8
libpgtcl - API для доступа к базе данных PostgreSQL из языка Tcl.

%description -l uk.UTF-8
libpgtcl - API для доступу до бази даних PostgreSQL з мови Tcl.

%package devel
Summary:	Development part of Tcl interface for PostgreSQL
Summary(pl.UTF-8):	Część dla programistów interfejsu Tcl dla PostgreSQL
Summary(ru.UTF-8):	Хедеры и библиотеки для разработок с использованием libpgtcl (Tcl интерфейс для PostgreSQL)
Summary(uk.UTF-8):	Хедери та бібліотеки для розробок з використанням libpgtcl (Tcl-інтерфейс для PostgreSQL)
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql-devel
Obsoletes:	postgresql-tcl-devel
Obsoletes:	postgresql-tcl-static

%description devel
Development part of Tcl interface for PostgreSQL.

%description devel -l pl.UTF-8
Część interfejsu Tcl dla PostgreSQL przeznaczona dla programistów.

%description devel -l ru.UTF-8
Это пакет разработчика для программирования с libpgtcl. Он включает
хедеры и библиотеки для использования в программах, которые используют
код или API libtcl (Tcl интерфейс для PostgreSQL).

%description devel -l uk.UTF-8
Це пакет програміста для програмування з libpgtcl. Він містить хедери
та бібліотеки для використання в програмах, які використовують код або
API libtcl (Tcl-інтерфейсу для PostgreSQL).

%prep
%setup -q -n pgtcl%{version}

# workaround for broken make install
touch doc/fake.n

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.async TODO
%dir %{_libdir}/pgtcl%{version}
%attr(755,root,root) %{_libdir}/pgtcl%{version}/libpgtcl%{version}.so
%{_libdir}/pgtcl%{version}/*.tcl

%files devel
%defattr(644,root,root,755)
%doc doc/{PGTCL-NOTES,libpgtcl.pdf} doc/html
%{_includedir}/libpgtcl.h
