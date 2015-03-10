%include	/usr/lib/rpm/macros.perl
Summary:	Program for efficient remote updates of backup sets
Summary(pl.UTF-8):	Program do wydajnego zdalnego uaktualniania zbiorów kopii zapasowych
Name:		rsnapshot
Version:	1.3.1
Release:	6
License:	GPL v2+
Group:		Daemons
Source0:	http://www.rsnapshot.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	588f92995dcf60a6ea6df8d94a017e7e
Patch0:		%{name}-pod.patch
Patch1:		%{name}-lockfile.patch
Patch2:		%{name}-pid.patch
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
%patch2 -p1

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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_mandir}/man1/*
