Name:    lxqt-panel
Summary: Main panel bar for LXQt desktop suite
Version: 0.9.0
Release: 1%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: http://downloads.lxqt.org/lxqt/0.9.0/lxqt-panel-0.9.0.tar.xz
Patch0:  lxqt-panel-0.8.0-lxqtmount-includes.patch

BuildRequires: cmake >= 2.8.9
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg) >= 1.0.0
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(lxqtmount)
BuildRequires: pkgconfig(lxqt-globalkeys)
BuildRequires: pkgconfig(lxqt-globalkeys-ui)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libstatgrab)
BuildRequires: pkgconfig(sysstat-qt5)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: kf5-kguiaddons-devel >= 5.5.0 
BuildRequires: desktop-file-utils

Requires: lxqt-runner >= %{version}
Requires: lxqt-common >= 0.9.0

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup
%patch0 -p1 -b .header

%build
rm plugin-mount/translations/mount_ru_RU.desktop
rm plugin-networkmonitor/translations/networkmonitor_de_DE.desktop

mkdir -p %{_target_platform}
pushd %{_target_platform}
	%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

for desktop in %{buildroot}/%{_datadir}/lxqt/lxqt-panel/*.desktop; do
	# Exclude category as been Service 
	desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
done

%files
%doc COPYING
%{_bindir}/lxqt-panel
%dir %{_libdir}/lxqt-panel
%{_libdir}/lxqt-panel/*.so
%{_datadir}/lxqt
%dir %{_sysconfdir}/xdg/lxqt
%config(noreplace) %{_sysconfdir}/xdg/lxqt/panel.conf

%files devel
%{_includedir}/lxqt

%changelog
* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Preparing 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-8
- Rebuild against new Qt 5.4.0

* Sat Dec 20 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-7
- Unify naming as discussed on Fedora IRC

* Tue Dec 16 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-6
- Wrong requires of xscreensaver-base. Should be handled but xdg-utils

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Fix missing item on  https://bugzilla.redhat.com/show_bug.cgi?id=1159873 - dir ownership

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- New update to match requests on https://bugzilla.redhat.com/show_bug.cgi?id=1159873

* Tue Nov 04 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update to match requests on review https://bugzilla.redhat.com/show_bug.cgi?id=1159873

* Mon Nov 03 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Update to review on Fedora bugzilla
- Added upstream patch #288 # https://github.com/lxde/lxde-qt/issues/288

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
