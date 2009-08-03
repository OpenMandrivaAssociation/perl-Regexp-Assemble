%define upstream_name    Regexp-Assemble
%define upstream_version 0.34

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Assemble multiple Regular Expressions into a single RE
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
rm -f eg/hostmatch/error.canonical
chmod 755 eg/unquotemeta
perl -pi -e s,/usr/local/bin/perl,/usr/bin/perl, eg/* eg/hostmatch/*
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README TODO eg
%{perl_vendorlib}/Regexp
%{_mandir}/*/*
