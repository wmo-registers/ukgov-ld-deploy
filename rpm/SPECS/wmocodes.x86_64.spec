
Name:		wmocodes
Version:	3.0
Release:	3
Summary:	wmocodes linked data registry

License:	apache
URL:		https://github.com/wmo-registers/ukgov-ld-deploy
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	registry-core

%description
wmocodes instance of ukgov-ld linked data registry


%prep
%setup -q 



%install
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/opt/ldregistry/
cp -r templates $RPM_BUILD_ROOT/opt/ldregistry/
cp -r ui $RPM_BUILD_ROOT/opt/ldregistry/
            

%pre
service tomcat7 stop

%clean
rm -rf $RPM_BUILD_ROOT/*

%post
sed -i -e 's/http:\/\/ukgovld-registry.dnsalias.net\//http:\/\/codes.wmo.int\//' /opt/ldregistry/config/services.conf
service tomcat7 start


%files

%defattr(775,root,tomcat,-)
/opt/ldregistry/ui/img/wmo-logo-official-blue-on-white-trunc.png
/opt/ldregistry/templates/about.vm
/opt/ldregistry/templates/header.vm
/opt/ldregistry/templates/main.vm
/opt/ldregistry/templates/navbar.vm
/opt/ldregistry/templates/root.vm
/opt/ldregistry/ui/css/bootstrap.css
/opt/ldregistry/ui/css/bootstrap.min.css
/opt/ldregistry/ui/css/ui.css
/opt/ldregistry/ui/resources/observableProperty_MeteorologicalAerodromeForecast.xml
/opt/ldregistry/ui/resources/observableProperty_MeteorologicalAerodromeObservation.xml
/opt/ldregistry/ui/resources/observableProperty_MeteorologicalAerodromeTrendForecast.xml
/opt/ldregistry/ui/resources/WMO-Codes-Registry_FAQ-v1.0.pdf
/opt/ldregistry/ui/resources/WMO-Codes-Registry_user-guide-v1.0.pdf


%changelog
* Thu Jul 03 2014 mark h <markh@metarelate.net> - 1.0-1
- Initial version
