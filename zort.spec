# TODO: add other webserver-support (lighttpd, etc.)
Summary:	Zort is another in a long line of web-based RSS/Atom aggregators
Summary(hu.UTF-8):	Zort egy a web alapú RSS/Atom olvasók hosszú sorában
Name:		zort
Version:	1.1.0
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/zort/%{name}-%{version}.tar.gz
# Source0-md5:	823ced7234b12f81698393c2e35d75d6
URL:		http://munin.sourceforge.net/
Requires:	webserver
Requires:	webserver(php)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# TODO
# maybe other directory use of lighttpd ?
%define		htmldir		/home/services/httpd/html/%{name}

%description
Zort is another in a long line of web-based RSS/Atom aggregators,
based on MagpieRSS. It features:

- Minimal interface
- Everything on one page
- Clean-looking CSS and Javascript to hide/show whatever feeds you
  want to view at the time
- The usual caching, etc.

It does not feature:

- A database backend
- Support for multiple users
- A set of administrative screens
- An authentication system of any kind
- Flagging of RSS items as read/saved/etc


%description -l hu.UTF-8
Zort egy a sok web alapú RSS/Atom olvasó között. A MagpieRSS-re épül.
Lehetőségei:

- egyszerű interface
- minden egy lapon
- egyszerű CSS és Javascript, amelyekkel elrejtheted/megnézheted
  azokat a forrásokat, amelyeket egyszerre akarsz látni
- szokásos cache, stb.

Nem lehetőségei:

- adatbázis háttér
- több user
- adminisztrátor képernyők
- bármely autentikációs rendszer
- RSS elemek cimkézése (úgymint olvasott/mentett/stb.)

%package examples
Summary:	Zort example config files
Summary(hu.UTF-8):	Zort példa konfig fájlok
Group:		Applications/Networking

%description examples
Zort example config files.

%description -l hu.UTF-8
Zort példa konfig fájlok


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{htmldir}/cache
install *.png index.php $RPM_BUILD_ROOT%{htmldir}

install -d $RPM_BUILD_ROOT%{htmldir}/magpierss/extlib
install magpierss/*.{inc,patch} $RPM_BUILD_ROOT%{htmldir}/magpierss
install magpierss/extlib/* $RPM_BUILD_ROOT%{htmldir}/magpierss/extlib
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%version
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%version

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Please don't forget to create a config file named %{htmldir}/config.php!"
echo "See zort-examples package!"

%files
%defattr(644,root,root,755)
# TODO
# or other user when you use another webserver than apache
%attr(775,http,http) %dir %{htmldir}
%attr(775,http,http) %dir %{htmldir}/cache
%{htmldir}/*.png
%{htmldir}/index.php

%dir %{htmldir}/magpierss
%dir %{htmldir}/magpierss/extlib
%{htmldir}/magpierss/*.inc
%{htmldir}/magpierss/*.patch
%{htmldir}/magpierss/extlib/*

%doc docs/AUTHORS docs/ChangeLog docs/INSTALL docs/TODO

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
