%bcond_without	tests
Summary:	Program for efficient remote updates of backup sets
Summary(pl.UTF-8):	Program do wydajnego zdalnego uaktualniania zbiorów kopii zapasowych
Name:		rsnapshot
Version:	1.4.2
Release:	2
License:	GPL v2+
Group:		Daemons
Source0:	http://www.rsnapshot.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	860382f19e38fc649f9447397b54e442
Patch0:		bug-207.patch
Patch1:		pid.patch
URL:		http://www.rsnapshot.org/
BuildRequires:	rpm-perlprov
Requires:	rsync
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rsnapshot is an efficient backup program built on rsync.

%description -l pl.UTF-8
rsnapshot to wydajny program do wykonywania kopii zapasowych stworzony
w oparciu o rsynca.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	RSYNC=%{_bindir}/rsync
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p utils/rsnapreport.pl $RPM_BUILD_ROOT%{_bindir}

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf{.default,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/rsnapreport.pl
%attr(755,root,root) %{_bindir}/rsnapshot
%attr(755,root,root) %{_bindir}/rsnapshot-diff
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rsnapshot.conf
%{_mandir}/man1/rsnapshot-diff.1*
%{_mandir}/man1/rsnapshot.1*
