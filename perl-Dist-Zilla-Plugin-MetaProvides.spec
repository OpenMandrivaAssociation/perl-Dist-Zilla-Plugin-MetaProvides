%define upstream_name    Dist-Zilla-Plugin-MetaProvides
%define upstream_version 2.000000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	When nothing else works, pull in hand-crafted metadata from a specified file

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Discover)
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(ExtUtils::Manifest) >= 1.560.0
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Module::Extract::Namespaces)
BuildRequires:	perl(Module::Extract::VERSION)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
#BuildRequires:	perl(MooseX::Declare)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(Path::Class::Dir)
BuildRequires:	perl(Path::Class::File)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(YAML::Tiny)
BuildRequires:	perl(aliased)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

Requires: perl(Module::Extract::Namespaces)
Requires: perl(Module::Extract::VERSION)
Requires: perl(aliased)

%description
This Distribution Contains a small bundle of plugins for various ways of
populating the 'META.yml' that is built with your distribution.

The initial reason for this is due to stuff that uses the MooseX::Declare
manpage style class definitions not being parseable by many tools upstream,
so this is here to cover this problem by defining it in the metadata.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


