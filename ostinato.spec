%global _hardened_build 1

%define _qmake qmake
%if 0%{?fedora} >= 21
%define _qmake qmake-qt4
%endif
%if 0%{?rhel} || 0%{?centos}
%ifarch x86_64
%define _qmake /usr/lib64/qt4/bin/qmake
%else
%define _qmake /usr/lib/qt4/bin/qmake
%endif
%endif

Name:           ostinato
Version:        0.7.1
Release:        4%{?dist}
License:        GPL-3.0+
Summary:        Packet/Traffic Generator and Analyzer
Url:            http://code.google.com/p/ostinato/
Group:          Productivity/Networking/Diagnostic
Source0:        http://dl.bintray.com/pstavirs/ostinato/%{name}-src-%{version}.tar.gz
%if 0%{?centos} || 0%{?fedora} || 0%{?rhel}
BuildRequires:  gcc-c++
%endif
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  qt-devel
BuildRequires:  protobuf-devel >= 2.3
%if 0%{?centos} || 0%{?fedora} || 0%{?rhel}
Requires:       wireshark
%endif
Requires:		%{name}-server = %{version}-%{release}
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
Ostinato is a network packet/traffic generator and analyzer
with a friendly GUI. It aims to be "Wireshark in Reverse"
and thus become complementary to Wireshark. It features custom
packet crafting with editing of any field for several protocols:
Ethernet, 802.3, LLC SNAP, VLAN (with Q-in-Q), ARP, IPv4, IPv6,
IP-in-IP a.k.a IP Tunneling, TCP, UDP, ICMPv4, ICMPv6, IGMP, MLD,
HTTP, SIP, RTSP, NNTP, etc. It is useful for both functional and
performance testing.

%package server
Group:          Productivity/Networking/Diagnostic
Summary:        Drone server for Ostinato Packet/Traffic Generator and Analyzer
%description server
Drone server for the Ostinato packet/traffic generator.
Ostinato is a network packet/traffic generator and analyzer
with a friendly GUI. It aims to be "Wireshark in Reverse"
and thus become complementary to Wireshark. It features custom
packet crafting with editing of any field for several protocols:
Ethernet, 802.3, LLC SNAP, VLAN (with Q-in-Q), ARP, IPv4, IPv6,
IP-in-IP a.k.a IP Tunneling, TCP, UDP, ICMPv4, ICMPv6, IGMP, MLD,
HTTP, SIP, RTSP, NNTP, etc. It is useful for both functional and
performance testing.

%prep
%setup -q

# Fix permissions (fix for rpmlint warning "spurious-executable-perm")
chmod 644 COPYING

%build
%{_qmake} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files server
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/drone

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/ostinato

%changelog
* Tue Dec 29 2015 John Siegrist <john@complects.com> - 0.7.1-4
- Updated project BuildRequires dependencies
* Wed Dec 16 2015 Jay Turner <jkt@iix.net> - 0.7.1-3
- Initial build for CloudRouter project
* Fri Jun 29 2012 asterios.dramis@gmail.com
- Recommend instead of Require wireshark (not mandatory) for openSUSE and
  Mandriva.
* Fri Jun 15 2012 asterios.dramis@gmail.com
- Changes on spec file based on spec-cleaner run.
- Updated License: to GPL-3.0+.
- Removed gcc-c++ indirect build dependency for openSUSE and Mandriva (not
  needed).
- Install and fix permissions of COPYING file (fix for rpmlint warning
  "spurious-executable-perm") (done for all distributions).
- Fixed openSUSE rpm post build check warning "File is compiled without
  RPM_OPT_FLAGS".
- Added a desktop file for openSUSE using xdg-su for executing ostinato.
  Install also a temporary icon (using ImageMagick to fix its size).
