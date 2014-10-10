%define upstream_name    Regexp-Assemble
%define upstream_version 0.35

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Assemble multiple Regular Expressions into a single RE
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Regexp::Assemble takes an arbitrary number of regular expressions and assembles
them into a single regular expression (or RE) that will match all that each of
the individual REs match. As a result, instead of having a large list of
expressions to loop over, the string only needs to be tested against one
expression. This is interesting when you have several thousand patterns to deal
with. Serious effort is made to produce the smallest pattern possible. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -f eg/hostmatch/error.canonical
chmod 755 eg/unquotemeta
perl -pi -e s,/usr/local/bin/perl,/usr/bin/perl, eg/* eg/hostmatch/*
%makeinstall_std

%files
%doc Changes README TODO eg
%{perl_vendorlib}/Regexp
%{_mandir}/*/*


%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.350.0-1mdv2011.0
+ Revision: 654291
- update to new version 0.35

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2010.0
+ Revision: 408042
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2009.0
+ Revision: 224889
- new version

* Sun Jun 08 2008 Olivier Thauvin <nanardon@mandriva.org> 0.33-1mdv2009.0
+ Revision: 216914
- 0.33

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Funda Wang <fwang@mandriva.org> 0.32-1mdv2008.0
+ Revision: 60484
- New version 0.32

* Mon Jul 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.31-1mdv2008.0
+ Revision: 46900
- 0.31


* Tue Dec 12 2006 Olivier Thauvin <nanardon@mandriva.org> 0.28-1mdv2007.0
+ Revision: 96025
- 0.28
- Import perl-Regexp-Assemble

* Fri Aug 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2007.0
- New version 0.26

* Thu Apr 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdk
- New release 0.25
- better source URL

* Wed Mar 22 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.24-1mdk
- 0.24

* Wed Jan 11 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.23-1mdk
- 0.23

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.22-1mdk
- 0.22

* Wed Nov 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.21-1mdk
- 0.21

* Wed Nov 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.20-1mdk
- 0.20

* Thu Oct 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdk
- new version
- rpmbuildupdate aware
- fix directory ownership

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.17-1mdk
- 0.17

* Wed Aug 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- 0.16

* Fri Apr 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-1mdk
- Initial MDK release.

