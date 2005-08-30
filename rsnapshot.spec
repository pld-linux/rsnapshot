Summary:	Program for efficient remote updates of backup sets
Summary(pl):	Program do wydajnego zdalnego uaktualniania zbiorów kopii zapasowych
Name:		rsnapshot
Version:	1.2.3
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://www.rsnapshot.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	b27d90886b25d0e160b267f98c605aec
URL:		http://www.rsnapshot.org/
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
%doc README AUTHORS TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
