%if 0%{?rhel} == 6
%define cmake_pkg cmake28
%else
%define cmake_pkg cmake
%endif

Name:    lxqt-panel
Summary: Main panel bar for LXQt desktop suite
Version: 0.8.0
Release: 7%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: http://lxqt.org/downloads/lxqt/0.8.0/%{name}-%{version}.tar.xz
Patch0:  lxqt-panel-0.8.0-unify.patch
Patch1:  lxqt-panel-0.8.0-desktop-files.patch
# https://github.com/lxde/lxde-qt/issues/288
Patch100: lxqt-panel-0.8.0-undefined-references.patch
Patch101: lxqt-panel-0.8.0-lxqtmount-includes.patch

BuildRequires: %{cmake_pkg} >= 2.8.9
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg) >= 1.0.0
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(lxqtmount)
BuildRequires: pkgconfig(lxqt-globalkeys)
BuildRequires: pkgconfig(lxqt-globalkeys-ui)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libstatgrab)
BuildRequires: pkgconfig(sysstat-qt5)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: desktop-file-utils

Requires: lxqt-runner >= %{version}
Requires: lxqt-common >= 0.8.0

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup
%patch0 -p1 -b .unify
%patch1 -p1 -b .desktp_patch
%patch100 -p1 -b .upstream-references
%patch101 -p1 -b .upstream-includes

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{?cmake28}%{!?cmake28:%{?cmake}} -DUSE_QT5=TRUE ..
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
