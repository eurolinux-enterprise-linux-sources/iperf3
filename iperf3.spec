Name:	iperf3
Version: 3.1.7
Release: 2%{?dist}
Summary: Measurement tool for TCP/UDP bandwidth performance

Group:	 Applications/Internet	
License: BSD	
URL:	 http://downloads.es.net/pub/iperf/
Source0: http://downloads.es.net/pub/iperf/iperf-%{version}.tar.gz

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
various parameters and UDP characteristics. Iperf reports bandwidth, delay
jitter, data-gram loss.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       iperf3 = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n iperf-%{version}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall -C src INSTALL_DIR="${RPM_BUILD_ROOT}%{_bindir}"
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libiperf.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libiperf.a

%files
%defattr(-,root,root,-)
%%doc README.md INSTALL LICENSE RELEASE_NOTES
%{_mandir}/man1/iperf3.1.gz
%{_mandir}/man3/libiperf.3.gz
%{_bindir}/iperf3
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/iperf_api.h
%{_libdir}/*.so

%changelog
* Fri Mar 10 2017 Michal Ruprich - 3.1.7-2
- Related: #913329 - [RFE] include iperf3 in RHEL 7
                   - adding requires to spec file for devel package

* Thu Mar 09 2017 Michal Ruprich <mruprich@redhat.com> - 3.1.7-1
- Related: #913329 - [RFE] include iperf3 in RHEL 7
                   - adding latest version before including iperf3 in RHEL-7

* Wed Mar 01 2017 Michal Ruprich <mruprich@redhat.com> - 3.1.6-1
- Resolves: #913329 - [RFE] include iperf3 in RHEL 7
- initial build
