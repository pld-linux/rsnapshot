Summary:	Program for efficient remote updates of backup sets
Summary(pl):	Program do wydajnego zdalnego uaktualniania zbiorów kopii zapasowych
Name:		rsnapshot
Version:	1.0.2
Release:	1
License:	GPL
Group:		Daemons
Source0:	 http://rsnapshot.scubaninja.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	d30a2abf6b58416b7258a80f50a78c59
Requires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rsnapshot is an efficient backup program built on rsync.

%description -l pl
rsnapshot to wydajny program do wykonywania kopii zapasowych stworzony
w oparciu o rsynca.

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

install rsnapshot $RPM_BUILD_ROOT%{_bindir}/rsnapshot
install rsnapshot.conf $RPM_BUILD_ROOT%{_sysconfdir}/rsnapshot.conf
install rsnapshot.1 $RPM_BUILD_ROOT%{_mandir}/man1/rsnapshot.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
