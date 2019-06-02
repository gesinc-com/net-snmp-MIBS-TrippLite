
Summary:        Tripp Lite Enterprise MIB Package
Name:           net-snmp-mibs-tripplite
Version:        15.5.3
Release:        2
Epoch:          0

Group:          System Environment/Daemons
License:        unknown; (c) 2018 by Tripp Lite 
URL:            https://www.tripplite.com

Source0:        https://assets.tripplite.com/firmware/tripplite-mib.zip

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       net-snmp

%description
(from https://www.tripplite.com/products/management-utilities)
Tripp Lite Enterprise MIB Package


%prep
%setup -qc


#build

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} \
    $RPM_BUILD_ROOT%{_datadir}/snmp/mibs/

for name in MIBs/*.MIB
do
  install ${name} \
  $RPM_BUILD_ROOT%{_datadir}/snmp/mibs/${name}.txt
done


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc MIBs/README-MIB.txt
%{_datadir}/snmp/mibs/*


%changelog
* Sat Jun 01 2019 Bishop <bishopolis@gmail.com> - 0:15.5.3-0
- Initial RPM release.

