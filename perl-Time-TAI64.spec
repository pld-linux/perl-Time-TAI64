#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Time
%define		pnam	TAI64
%include	/usr/lib/rpm/macros.perl
Summary:	Time::TAI64 - Perl extension for converting TAI64 strings into standard unix timestamps
Name:		perl-Time-TAI64
Version:	2.11
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f91734171a72b418bd70456fda487ce
Source1:	tai64nd.pl
URL:		http://search.cpan.org/dist/Time-TAI64/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package provides routines to convert TAI64 strings, like
timestamps produced by multilog, into values that can be processed by
other perl functions to display the timestamp in human-readable form
and/or use in mathematical computations.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}/tai64nd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_sbindir}/tai64nd
%{perl_vendorlib}/Time/TAI64.pm
%{_mandir}/man3/Time::TAI64.3pm*
