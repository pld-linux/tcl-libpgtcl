Summary:	Tcl interface for PostgreSQL
Summary(es):	Bibliotecas y shell Tcl para acceder un servidor PostgreSQL
Summary(pl):	Interfejs Tcl dla PostgreSQL
Summary(pt_BR):	Bibliotecas e shell para programas em Tcl acessarem o servidor PostgreSQL
Summary(ru):	���������� ��� ������� � PostgreSQL �� Tcl
Summary(uk):	��̦����� ��� ������� �� PostgreSQL � Tcl
Summary(zh_CN):	һ�� Tcl ��� PostgreSQL �� PL/Tcl �������
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
libpgtcl - API ��� ������� � ���� ������ PostgreSQL �� ����� Tcl.

%description -l uk
libpgtcl - API ��� ������� �� ���� ����� PostgreSQL � ���� Tcl.

%package devel
Summary:	Development part of Tcl interface for PostgreSQL
Summary(pl):	Cz�� dla programist�w interfejsu Tcl dla PostgreSQL
Summary(ru):	������ � ���������� ��� ���������� � �������������� libpgtcl (Tcl ��������� ��� PostgreSQL)
Summary(uk):	������ �� ¦�̦����� ��� �������� � ������������� libpgtcl (Tcl-��������� ��� PostgreSQL)
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql-devel
Obsoletes:	postgresql-tcl-devel
Obsoletes:	postgresql-tcl-static

%description devel
Development part of Tcl interface for PostgreSQL.

%description devel -l pl
Cz�� interfejsu Tcl dla PostgreSQL przeznaczona dla programist�w.

%description devel -l ru
��� ����� ������������ ��� ���������������� � libpgtcl. �� ��������
������ � ���������� ��� ������������� � ����������, ������� ����������
��� ��� API libtcl (Tcl ��������� ��� PostgreSQL).

%description devel -l uk
�� ����� ������ͦ��� ��� ������������� � libpgtcl. ��� ͦ����� ������
�� ¦�̦����� ��� ������������ � ���������, �˦ �������������� ��� ���
API libtcl (Tcl-���������� ��� PostgreSQL).

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
