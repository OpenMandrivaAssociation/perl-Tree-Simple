%define upstream_name    Tree-Simple
%define upstream_version 1.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A simple tree object
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Tree/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Test-Exception
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a fully object-oriented implementation of a simple n-ary tree.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Tree/Simple/*
%{perl_vendorlib}/Tree/Simple.pm
%{_mandir}/*/*
