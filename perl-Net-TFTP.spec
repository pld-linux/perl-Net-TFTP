#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	TFTP
Summary:	Net::TFTP Perl module
Summary(cs.UTF-8):	Modul Net::TFTP pro Perl
Summary(da.UTF-8):	Perlmodul Net::TFTP
Summary(de.UTF-8):	Net::TFTP Perl Modul
Summary(es.UTF-8):	Módulo de Perl Net::TFTP
Summary(fr.UTF-8):	Module Perl Net::TFTP
Summary(it.UTF-8):	Modulo di Perl Net::TFTP
Summary(ja.UTF-8):	Net::TFTP Perl モジュール
Summary(ko.UTF-8):	Net::TFTP 펄 모줄
Summary(nb.UTF-8):	Perlmodul Net::TFTP
Summary(pl.UTF-8):	Moduł Perla Net::TFTP
Summary(pt.UTF-8):	Módulo de Perl Net::TFTP
Summary(pt_BR.UTF-8):	Módulo Perl Net::TFTP
Summary(ru.UTF-8):	Модуль для Perl Net::TFTP
Summary(sv.UTF-8):	Net::TFTP Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Net::TFTP
Summary(zh_CN.UTF-8):	Net::TFTP Perl 模块
Name:		perl-Net-TFTP
Version:	0.16
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	59d0faa69e894a99fc402bbda4ca7734
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::TFTP - TFTP Client.

%description -l pl.UTF-8
Net::TFTP - klient TFTP.

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
