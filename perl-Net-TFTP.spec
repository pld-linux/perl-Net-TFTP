#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	TFTP
Summary:	Net::TFTP Perl module
Summary(cs):	Modul Net::TFTP pro Perl
Summary(da):	Perlmodul Net::TFTP
Summary(de):	Net::TFTP Perl Modul
Summary(es):	Módulo de Perl Net::TFTP
Summary(fr):	Module Perl Net::TFTP
Summary(it):	Modulo di Perl Net::TFTP
Summary(ja):	Net::TFTP Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Net::TFTP ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Net::TFTP
Summary(pl):	Modu³ Perla Net::TFTP
Summary(pt):	Módulo de Perl Net::TFTP
Summary(pt_BR):	Módulo Perl Net::TFTP
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Net::TFTP
Summary(sv):	Net::TFTP Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Net::TFTP
Summary(zh_CN):	Net::TFTP Perl Ä£¿é
Name:		perl-Net-TFTP
Version:	0.16
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	59d0faa69e894a99fc402bbda4ca7734
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::TFTP - TFTP Client.

%description -l pl
Net::TFTP - klient TFTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net/TFTP.pm
%{_mandir}/man3/*
