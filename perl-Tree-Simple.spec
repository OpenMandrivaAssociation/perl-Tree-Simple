%define upstream_name    Tree-Simple
%define upstream_version 1.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:	A simple tree object
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Tree/Tree-Simple-%{upstream_version}.tgz

BuildRequires:	perl-Test-Exception
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module in an fully object-oriented implementation of a simple n-ary tree.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Tree/Simple/*
%{perl_vendorlib}/Tree/Simple.pm
%{_mandir}/*/*


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2010.0
+ Revision: 408094
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.18-4mdv2009.0
+ Revision: 258706
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.18-3mdv2009.0
+ Revision: 246664
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2008.1
+ Revision: 109577
- update to new version 1.18


* Mon Dec 11 2006 Olivier Thauvin <nanardon@mandriva.org> 1.17-1mdv2007.0
+ Revision: 94586
- 1.17
- Import perl-Tree-Simple

* Mon Feb 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.16-1mdk
- 1.16

* Tue May 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.15-1mdk
- 1.15

* Wed May 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.14-1mdk
- First Mandriva release


