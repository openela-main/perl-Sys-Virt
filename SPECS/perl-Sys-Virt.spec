# Automatically generated by perl-Sys-Virt.spec.PL

Name:           perl-Sys-Virt
Version:        8.0.0
Release:        1%{?dist}
Summary:        Represent and manage a libvirt hypervisor connection
License:        GPLv2+ or Artistic
URL:            https://metacpan.org/release/Sys-Virt
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Sys-Virt-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libvirt-devel >= %{version}
BuildRequires:  make
BuildRequires:  perl-devel
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
%endif
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::XPath::XMLParser)
# Optional tests only
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  git
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
The Sys::Virt module provides a Perl XS binding to the libvirt virtual
machine management APIs. This allows machines running within arbitrary
virtualization containers to be managed with a consistent API.

%prep
%autosetup -S git -n Sys-Virt-v%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc AUTHORS Changes README examples/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys*
%{_mandir}/man3/*

%changelog
* Fri Jan 14 2022 Daniel P. Berrangé <berrange@redhat.com> - 8.0.0-1
- Rebase to 8.0.0 release
- Resolves: rhbz#2012813

* Tue Dec  7 2021 Daniel P. Berrangé <berrange@redhat.com> - 7.10.0-1
- Rebase to 7.10.0 release
- Resolves: rhbz#2012813

* Tue Dec  7 2021 Daniel P. Berrangé <berrange@redhat.com> - 7.8.0-2
- Fix bug passing flags when creating NWFilterBinding
- Resolves: rhbz#2029647

* Tue Oct 19 2021 Daniel P. Berrangé <berrange@redhat.com> - 7.8.0-1
- Rebase to 7.8.0 release
- Resolves: rhbz#2012813

* Thu Sep 2 2021 Danilo C. L. de Paula <ddepaula@redhat.com> - 7.4.0-1.el8
- Resolves: bz#2000225
  (Rebase virt:rhel module:stream based on AV-8.6)

* Mon Apr 27 2020 Danilo C. L. de Paula <ddepaula@redhat.com> - 6.0.0
- Resolves: bz#1810193
  (Upgrade components in virt:rhel module:stream for RHEL-8.3 release)

* Fri Jun 28 2019 Danilo de Paula <ddepaula@redhat.com> - 4.5.0-5
- Rebuild all virt packages to fix RHEL's upgrade path
- Resolves: rhbz#1695587
  (Ensure modular RPM upgrade path)

* Wed Aug 29 2018 Daniel P. Berrangé <berrange@redhat.com> - 4.5.0-4
- Fix typed parameter memory handling (rhbz #1602346)
- Fix missing NWFilterBinding module (rhbz #1615841)

* Tue Aug  7 2018 Danilo de Paula <ddepaula@redhat.com> - 4.5.0-3
- Included BuildRequire: git to fix a building issue

* Tue Aug  7 2018 Daniel P. Berrangé <berrange@redhat.com> - 4.5.0-2
- Fix typed parameter memory handling (rhbz#1602346)

* Tue Jul  3 2018 Daniel P. Berrangé <berrange@redhat.com> - 4.5.0-1
- Update to 4.5.0 release

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.4.0-2
- Perl 5.28 rebuild

* Tue Apr  3 2018 Daniel P. Berrangé <berrange@redhat.com> - 4.2.0-1
- Update to 4.2.0 release

* Mon Mar  5 2018 Daniel P. Berrange <berrange@redhat.com> - 4.1.0-1
- Update to 4.1.0 release

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.0.0-3
- Add build-require gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Daniel P. Berrange <berrange@redhat.com> - 4.0.0-1
- Update to 4.0.0 release

* Tue Dec  5 2017 Daniel P. Berrange <berrange@redhat.com> - 3.9.1-1
- Update to 3.9.1 release

* Fri Nov  3 2017 Daniel P. Berrange <berrange@redhat.com> - 3.9.0-1
- Update to 3.9.0 release

* Wed Oct  4 2017 Daniel P. Berrange <berrange@redhat.com> - 3.8.0-1
- Update to 3.8.0 release

* Mon Sep  4 2017 Daniel P. Berrange <berrange@redhat.com> - 3.7.0-1
- Update to 3.7.0 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul  6 2017 Daniel P. Berrange <berrange@redhat.com> - 3.5.0-1
- Update to 3.5.0 release

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.0-2
- Perl 5.26 rebuild

* Mon Jun  5 2017 Daniel P. Berrange <berrange@redhat.com> - 3.4.0-1
- Update to 3.4.0 release

* Mon May  8 2017 Daniel P. Berrange <berrange@redhat.com> - 3.3.0-1
- Update to 3.3.0 release

* Mon Apr  3 2017 Daniel P. Berrange <berrange@redhat.com> - 3.2.0-1
- Update to 3.2.0 release

* Fri Mar  3 2017 Daniel P. Berrange <berrange@redhat.com> - 3.1.0-1
- Update to 3.1.0 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Daniel P. Berrange <berrange@redhat.com> - 3.0.0-1
- Update to 3.0.0 release

* Mon Dec  5 2016 Daniel P. Berrange <berrange@redhat.com> - 2.5.0-1
- Update to 2.5.0 release

* Wed Nov  2 2016 Daniel P. Berrange <berrange@redhat.com> - 2.4.0-1
- Update to 2.4.0 release

* Thu Oct  6 2016 Daniel P. Berrange <berrange@redhat.com> - 2.3.0-1
- Update to 2.3.0 release

* Mon Sep  5 2016 Daniel P. Berrange <berrange@redhat.com> - 2.2.0-1
- Update to 2.2.0 release

* Tue Aug  2 2016 Daniel P. Berrange <berrange@redhat.com> - 2.1.0-1
- Update to 2.1.0 release

* Fri Jul  1 2016 Daniel P. Berrange <berrange@redhat.com> - 2.0.0-1
- Update to 2.0.0 release

* Tue Jun  7 2016 Daniel P. Berrange <berrange@redhat.com> - 1.3.5-1
- Update to 1.3.5 release

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.4-2
- Perl 5.24 rebuild

* Wed May  4 2016 Daniel P. Berrange <berrange@redhat.com> - 1.3.4-1
- Update to 1.3.4 release

* Thu Apr  7 2016 Daniel P. Berrange <berrange@redhat.com> - 1.3.3-1
- Update to 1.3.3 release

* Tue Mar  1 2016 Daniel P. Berrange <berrange@redhat.com> - 1.3.2-1
- Update to 1.3.2 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Daniel P. Berrange <berrange@redhat.com> - 1.3.1-1
- Update to 1.3.1 release
