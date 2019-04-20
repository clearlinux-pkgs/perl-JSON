#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-JSON
Version  : 4.02
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/JSON-4.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/JSON-4.02.tar.gz
Summary  : JSON (JavaScript Object Notation) encoder/decoder
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
JSON - JSON (JavaScript Object Notation) encoder/decoder
SYNOPSIS
use JSON; # imports encode_json, decode_json, to_json and from_json.
# simple and fast interfaces (expect/generate UTF-8)
$utf8_encoded_json_text = encode_json $perl_hash_or_arrayref;
$perl_hash_or_arrayref  = decode_json $utf8_encoded_json_text;
# OO-interface
$json = JSON->new->allow_nonref;
$json_text   = $json->encode( $perl_scalar );
$perl_scalar = $json->decode( $json_text );
$pretty_printed = $json->pretty->encode( $perl_scalar ); # pretty-printing

%package dev
Summary: dev components for the perl-JSON package.
Group: Development
Provides: perl-JSON-devel = %{version}-%{release}
Requires: perl-JSON = %{version}-%{release}

%description dev
dev components for the perl-JSON package.


%prep
%setup -q -n JSON-4.02

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/JSON.pm
/usr/lib/perl5/vendor_perl/5.28.2/JSON/backportPP.pm
/usr/lib/perl5/vendor_perl/5.28.2/JSON/backportPP/Boolean.pm
/usr/lib/perl5/vendor_perl/5.28.2/JSON/backportPP/Compat5005.pm
/usr/lib/perl5/vendor_perl/5.28.2/JSON/backportPP/Compat5006.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/JSON.3
/usr/share/man/man3/JSON::backportPP.3
/usr/share/man/man3/JSON::backportPP::Boolean.3
/usr/share/man/man3/JSON::backportPP::Compat5005.3
/usr/share/man/man3/JSON::backportPP::Compat5006.3
