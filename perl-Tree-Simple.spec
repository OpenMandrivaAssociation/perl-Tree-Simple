%define realname Tree-Simple
%define name perl-%{realname}
%define version 1.18
%define release %mkrel 1

Summary:	A simple tree object
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Exception
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
This module in an fully object-oriented implementation of a simple n-ary tree.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Tree/Simple/*
%{perl_vendorlib}/Tree/Simple.pm
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT


