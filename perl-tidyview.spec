#
# Conditional build:
%bcond_with	tests		# perform "make test" (requires DISPLAY)

%define		pdir	tidyview
Summary:	Preview the effects of perltidy's plethora of options
Name:		perl-tidyview
Version:	1.14
Release:	1
License:	GPL-1.0+ or Artistic-1.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/L/LE/LEIF/tidyview-%{version}.tar.gz
# Source0-md5:	800c21347b8114e1990b03ceefed1b13
URL:		http://search.cpan.org/dist/tidyview/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Log::Log4perl) >= 1.0
BuildRequires:	perl(Tk::DiffText)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Preview the effects of perltidy's plethora of options.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/tidyview{.pl,}
mv $RPM_BUILD_ROOT%{_mandir}/man1/tidyview{.pl,}.1p

%{__rm} -r $RPM_BUILD_ROOT%{perl_vendorlib}/TidyView/t
%{__rm} -r $RPM_BUILD_ROOT%{perl_vendorlib}/PerlTidy/t

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/tidyview
%{_mandir}/man1/tidyview.1p*
%{_mandir}/man3/TidyView::Options.3pm*
%dir %{perl_vendorlib}/PerlTidy
%{perl_vendorlib}/PerlTidy/*.pm
%dir %{perl_vendorlib}/TidyView
%{perl_vendorlib}/TidyView/*.pm
