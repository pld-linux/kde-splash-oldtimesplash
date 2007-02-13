
%define		_splash		oldtimesplash

Summary:	KDE splash screen
Summary(pl.UTF-8):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=1214&id=1
Source0:	http://www.kde-look.org/content/files/1214-oldtimesplash.zip
# Source0-md5:	395d42f3aead26c3c9b21a328cd06dd6
Source1:	%{name}-Theme.rc
Source2:	%{name}-Preview.png
URL:		http://www.kde-look.org/content/show.php?content=1214
BuildRequires:	unzip
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A bit of "old styled" graphics for KDE splash may be a very good choice
if you are bored with all those blue themes around.

%description -l pl.UTF-8
Ekran startowy KDE "w starym stylu" może być bardzo dobrym wyborem jeżeli
czujesz się znudzony tymi wszystkimi motywami w niebieskich odcieniach.

%prep
%setup -q -c %{_splash} -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Theme.rc
install %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Preview.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
