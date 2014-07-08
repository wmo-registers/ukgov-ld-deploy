
Name:		ukgov-ld
Version:	1.0
Release:	4
Summary:	ukgov linked data registry

License:	apache
URL:		https://github.com/der/ukl-registry-poc
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	java-1.7.0-openjdk
Requires:	nginx
Requires:	tomcat7


%description
ukgov-ld linked data registry


%prep
%setup -q 


%install
rm -rf $RPM_BUILD_ROOT/*
install -D etc/sudoers.d/uklSudoers.conf $RPM_BUILD_ROOT/etc/sudoers.d/uklSudoers.conf
mkdir -p $RPM_BUILD_ROOT/var/local/registry/ui
install -D var/lib/tomcat7/webapps/ROOT.war $RPM_BUILD_ROOT/var/lib/tomcat7/webapps/ROOT.war

%pre

rm -rf /var/local/registry
alternatives --set java /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java
service tomcat7 stop

%post

service tomcat7 start

%clean
rm -rf $RPM_BUILD_ROOT/*


%files
/etc/sudoers.d/uklSudoers.conf
%defattr(775,root,tomcat,-)
/var/lib/tomcat7/webapps/ROOT.war
%dir /var/local/registry
%dir /var/local/registry/ui


%changelog
* Thu Aug 15 2013 Mark Hedley <mark.hedley@metoffice.gov.uk> - 1.0-1
- initial
- use nginx conf.d
