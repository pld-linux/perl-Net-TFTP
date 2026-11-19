#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	TFTP
Summary:	Net::TFTP Perl module - TFTP Client class
Summary(pl.UTF-8):	Moduł Perla Net::TFTP - klasa klienta TFTP
Name:		perl-Net-TFTP
Version:	0.1901
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1bab891330c443462fe4dad9e4365663
URL:		http://search.cpan.org/dist/Net-TFTP/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-MockModule >= 0.11
BuildRequires:	perl-Test-Warn
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::TFTP - TFTP Client class.

%description -l pl.UTF-8
Net::TFTP - klasa klienta TFTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net/TFTP.pm
%{_mandir}/man3/*
