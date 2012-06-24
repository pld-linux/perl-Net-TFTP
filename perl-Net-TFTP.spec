%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	TFTP
Summary:	Net-TFTP perl module
Summary(pl):	Modu� perla Net-TFTP
Name:		perl-Net-TFTP
Version:	0.13
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-TFTP - TFTP Client.

%description -l pl
Net-TFTP - klient TFTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/TFTP.pm
%{_mandir}/man3/*
