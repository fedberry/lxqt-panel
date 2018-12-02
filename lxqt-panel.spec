Name:    lxqt-panel
Summary: Main panel bar for LXQt desktop suite
Version: 0.13.0
Release: 5%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: https://github.com/lxde/lxqt-panel/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0: panel.conf.patch
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg) >= 1.0.0
BuildRequires: pkgconfig(lxqt) >= 0.13.0
BuildRequires: pkgconfig(lxqt-globalkeys)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libstatgrab)
BuildRequires: pkgconfig(sysstat-qt5)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(dbusmenu-qt5)
BuildRequires: kf5-kwindowsystem-devel >= 5.5.0
BuildRequires: kf5-kguiaddons-devel >= 5.5.0
BuildRequires: kf5-solid-devel >= 5.5.0
BuildRequires: desktop-file-utils
BuildRequires: lm_sensors-devel

Requires: lxmenu-data
Requires: lxqt-runner  >= 0.13.0
Requires: xscreensaver-base

Obsoletes: liblxqt-mount


%description
%{summary}.


%package devel
Summary:  Developer files for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: liblxqt-mount-devel <= 0.10.0


%description devel
%{summary}.


%prep
%autosetup -p1


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %{cmake_lxqt} \
    %if 0%{?rhel}
        -DKBINDICATOR_PLUGIN:BOOL=FALSE \
    %endif
    -DPULL_TRANSLATIONS=NO \
    ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%{_bindir}/lxqt-panel
%dir %{_libdir}/lxqt-panel
%{_libdir}/lxqt-panel/*.so
%{_datadir}/lxqt
%{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_sysconfdir}/xdg/menus/lxqt-applications.menu
%{_datadir}/desktop-directories/*.directory
%{_mandir}/man1/lxqt-panel*


%files devel
%dir %{_includedir}/lxqt
%{_includedir}/lxqt/*


%changelog
* Thu Nov 15 2018 Vaughan Agrez <devel at agrez dot net> - 0.13.0-5
- New version
- Bump release
- Update BuildRequires & Requires
- Drop patches 1,2 & 3
- Refactor panel.conf patch

* Mon Apr 02 2018 Vaughan Agrez <devel at agrez dot net> - 0.11.1-11
- Add fix for incorrect popup menu positions (Patch3)
- Update panel.conf patch

* Sun Mar 25 2018 Vaughan Agrez <devel at agrez dot net> - 0.11.1-10
- Set pavucontrol-qt as default pulseaudio mixer (Patch2)
- Revert default web browser to chromium

* Fri Dec 01 2017 Vaughan Agrez <devel at agrez dot net> - 0.11.1-9
- Set default web browser to firefox

* Tue Nov 28 2017 Vaughan Agrez <devel at agrez dot net> - 0.11.1-8
- Add patch for compiling against Qt 5.8
- Update Source0 url
- Bump release

* Sun May 14 2017 Vaughan Agrez <devel at agrez dot net> - 0.11.1-6
- Try to workaround "floating menu bug"

* Thu Apr 27 2017 Vaughan Agrez <devel at agrez dot net> - 0.11.1-5
- Update panel defaults (Patch0)
- Use %autosetup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-2
- Fix some rpmlint issues

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version 0.11.0

* Mon Sep 12 2016 Than Ngo <than@redhat.com> - 0.10.0-7
- requires on xscreensaver-base for the case only lxqt desktop is installed

* Tue May 24 2016 Than Ngo <than@redhat.com> 0.10.0-6
- add rhel support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-4
- Nor obsoletes razorqt anymore

* Sun Dec 13 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Disable kbindicator under epel

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Use new cmake_lxqt infra

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream version

* Thu Sep 17 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-8
- Rebuild due new libstatgrab soname.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-5
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Obsoletes typo

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-autosuspend and razorqt-appswitcher

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Obsoletes razorqt-panel as migrated to LXQt

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
