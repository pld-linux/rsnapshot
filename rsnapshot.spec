Summary:	Program for efficient remote updates of backup sets
Summary(pl):	Program do wydajnego zdalnego uaktualniania zbior�w kopii zapasowych
Name:		rsnapshot
Version:	1.0.10
Release:	1
License:	GPL
Group:		Daemons
Source0:	 http://rsnapshot.scubaninja.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	a63c052d4c4c601222f0a3de6d720b46
Requires:	perl-base
Requires:	rsync
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rsnapshot is an efficient backup program built on rsync.

%description -l pl
rsnapshot to wydajny program do wykonywania kopii zapasowych stworzony
w oparciu o rsynca.

%prep
%setup  -q

%build
%configure \
	RSYNC=rsync
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf{.default,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*