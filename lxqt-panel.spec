Name:    lxqt-panel
Summary: Main panel bar for LXQt desktop suite
Version: 0.10.0
Release: 1%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: http://downloads.lxqt.org/lxqt/%{version}/lxqt-panel-%{version}.tar.xz
Patch0:  lxqt-panel-0.10.0-translations-fix.patch

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
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(dbusmenu-qt5)
BuildRequires: kf5-kwindowsystem-devel >= 5.5.0
BuildRequires: kf5-kguiaddons-devel >= 5.5.0 
BuildRequires: kf5-solid-devel >= 5.5.0 
BuildRequires: desktop-file-utils

Requires: lxqt-runner >= %{version}
Requires: lxqt-common >= 0.9.0

%if 0%{?fedora} >= 22
Obsoletes: razorqt-panel <= 0.5.2
Obsoletes: razorqt-autosuspend <= 0.5.2
Obsoletes: razorqt-appswitcher <= 0.5.2
%endif
Obsoletes: liblxqt-mount <= 0.10.0

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: liblxqt-mount-devel <= 0.10.0

%description devel
%{summary}.

%prep
%setup
%patch0 -p1 -b .translations

%build
rm plugin-mount/translations/mount_ru.desktop 

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
%{_bindir}/lxqt-panel
%dir %{_libdir}/lxqt-panel
%{_libdir}/lxqt-panel/*.so
%{_datadir}/lxqt
%dir %{_sysconfdir}/xdg/lxqt
%config(noreplace) %{_sysconfdir}/xdg/lxqt/panel.conf

%files devel
%{_includedir}/lxqt

%changelog
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
