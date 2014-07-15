
Name:		wmocodes-bootstrap
Version:	1.2
Release:	4
Summary:	wmocodes linked data registry

License:	apache
URL:		https://github.com/wmo-registers/ukgov-ld-deploy
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	wmocodes

%description
wmocodes bootstrap data


%prep
%setup -q 



%install
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/opt/ldregistry/
cp -r boot $RPM_BUILD_ROOT/opt/ldregistry/
cp -r config $RPM_BUILD_ROOT/opt/ldregistry/
            

%pre

service tomcat7 stop
rm -rf /var/opt/ldregistry/store /var/opt/ldregistry/userstore /var/opt/ldregistry/logstore /var/opt/ldregistry/index



%clean
rm -rf $RPM_BUILD_ROOT/*

%post
service tomcat7 start

%files

%defattr(775,root,tomcat,-)
# current fix; future release of vanilla UKGovLD Registry should obviate need for this file
/opt/ldregistry/boot/system/bulkCollectionTypes/metadata.ttl
/opt/ldregistry/boot/system/bulkCollectionTypes/collectionTypes.ttl
# current fix; future release of vanilla UKGovLD Registry should obviate need for this file
/opt/ldregistry/boot/system/form-templates/metadata.ttl
# current fix; future release of vanilla UKGovLD Registry should obviate need for this file
/opt/ldregistry/boot/system/typed-templates/metadata.ttl
/opt/ldregistry/boot/system/organization/metadata.ttl
/opt/ldregistry/boot/system/organization/contents.ttl
# current fix; future release of vanilla UKGovLD Registry should obviate need for this file
/opt/ldregistry/boot/system/prefixes/metadata.ttl
/opt/ldregistry/boot/system/prefixes/wmo-prefixes-register.ttl
/opt/ldregistry/boot/system/metadata.ttl
/opt/ldregistry/boot/306/metadata.ttl
/opt/ldregistry/boot/306/4678/metadata.ttl
/opt/ldregistry/boot/306/4678/contents.ttl
/opt/ldregistry/boot/49-2/metadata.ttl
/opt/ldregistry/boot/49-2/AerodromePresentOrForecastWeather/metadata.ttl
/opt/ldregistry/boot/49-2/AerodromePresentOrForecastWeather/contents.ttl
/opt/ldregistry/boot/49-2/AerodromeRecentWeather/metadata.ttl
/opt/ldregistry/boot/49-2/AerodromeRecentWeather/contents.ttl
/opt/ldregistry/boot/49-2/CloudAmountReportedAtAerodrome/metadata.ttl
/opt/ldregistry/boot/49-2/CloudAmountReportedAtAerodrome/contents.ttl
/opt/ldregistry/boot/49-2/CloudAmountReportedAtAerodrome/contents2.ttl
/opt/ldregistry/boot/49-2/observable-property/metadata.ttl
/opt/ldregistry/boot/49-2/observable-property/contents.ttl
/opt/ldregistry/boot/49-2/observation-type/metadata.ttl
/opt/ldregistry/boot/49-2/observation-type/IWXXM/metadata.ttl
/opt/ldregistry/boot/49-2/observation-type/IWXXM/1.0/metadata.ttl
/opt/ldregistry/boot/49-2/observation-type/IWXXM/1.0/contents.ttl
/opt/ldregistry/boot/49-2/SigConvectiveCloudType/metadata.ttl
/opt/ldregistry/boot/49-2/SigConvectiveCloudType/contents.ttl
/opt/ldregistry/boot/49-2/SigWxPhenomena/metadata.ttl
/opt/ldregistry/boot/49-2/SigWxPhenomena/contents.ttl
/opt/ldregistry/boot/common/metadata.ttl
/opt/ldregistry/boot/common/nil/metadata.ttl
/opt/ldregistry/boot/common/nil/AboveDetectionRange.ttl
/opt/ldregistry/boot/common/nil/BelowDetectionRange.ttl
/opt/ldregistry/boot/common/nil/inapplicable.ttl
/opt/ldregistry/boot/common/nil/missing.ttl
/opt/ldregistry/boot/common/nil/noSignificantChange.ttl
/opt/ldregistry/boot/common/nil/notDetectedByAutoSystem.ttl
/opt/ldregistry/boot/common/nil/nothingOfOperationalSignificance.ttl
/opt/ldregistry/boot/common/nil/notObservable.ttl
/opt/ldregistry/boot/common/nil/template.ttl
/opt/ldregistry/boot/common/nil/unknown.ttl
/opt/ldregistry/boot/common/nil/withheld.ttl
/opt/ldregistry/boot/common/observation-type/metadata.ttl
/opt/ldregistry/boot/common/observation-type/METCE/metadata.ttl
/opt/ldregistry/boot/common/observation-type/METCE/2013/metadata.ttl
/opt/ldregistry/boot/common/observation-type/METCE/2013/contents.ttl
/opt/ldregistry/boot/common/observation-type/OGC-OM/metadata.ttl
/opt/ldregistry/boot/common/observation-type/OGC-OM/ogc-om-2.0.ttl
/opt/ldregistry/config/root-register.ttl
/opt/ldregistry/config/user.ini


%changelog
* Thu Jul 02 2014 mark h <markh@metarelate.net> - 1.0-1
- Initial version
