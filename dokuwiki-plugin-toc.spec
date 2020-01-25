%define		plugin		toc
%define		php_min_version 5.3.0
Summary:	DokuWiki TOC Action plugin
Summary(pl.UTF-8):	Wtyczka TOC Actiona dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20090413
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://projects.andriylesyuk.com/attachments/download/92/toc.tgz
# Source0-md5:	cd60c970e176372673ca401dde4ec02f
URL:		https://www.dokuwiki.org/plugin:toc
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20131208
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Dokuwiki pluging which allows to move TOC to the specified place in the page content.

%prep
%setup -qc
mv %{plugin}/* .

%build
version=$(awk -F"'" '/date/{print $4}' action.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{CREDITS,changelog}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
