#
# This file is edited from one generated automatically
#
Name     : hhvm
Version  : 3.17.2
Release  : 3
URL      : https://github.com/facebook/hhvm/archive/HHVM-3.17.2.tar.gz
Source0  : https://github.com/facebook/hhvm/archive/HHVM-3.17.2.tar.gz
Source1  : https://github.com/Cyan4973/lz4/archive/d86dc916771c126afb797637dda9f6421c0cb998.tar.gz
Source2  : https://github.com/MacPython/terryfy/archive/8bb673f4410819df06920fdcfd24e18d235d84f7.tar.gz
Source3  : https://github.com/ariya/FastLZ/archive/f1217348a868bdb9ee0730244475aee05ab329c5.tar.gz
Source4  : https://github.com/facebook/fatal/archive/e21df038e0b58855ef9344d1a3a4389e03ba2cc7.tar.gz
Source5  : https://github.com/facebook/fbthrift/archive/5e5773be567eeb53a75565a911ece7de2c89ee2b.tar.gz
Source6  : https://github.com/facebook/folly/archive/1d2d4f326acc0825690c151c38ac92d146b78146.tar.gz
Source7  : https://github.com/facebook/libafdt/archive/eb021a100e761616b35ad62c910d6c336e0711d2.tar.gz
Source8  : https://github.com/facebook/mcrouter/archive/dbf8878c0136e5f94e4bb0aef6f931d5aecfa74d.tar.gz
Source9  : https://github.com/facebook/mysql-5.6/archive/a9e580b5a0baa768210ef10544c8fab52003ec0b.tar.gz
Source10  : https://github.com/facebook/proxygen/archive/e3cdcb4db98d819465af487e9404a8a1032c2300.tar.gz
Source11  : https://github.com/facebook/rocksdb/archive/dcc898b0215cee3b1baa88149c1f39e37e9bfd09.tar.gz
Source12  : https://github.com/facebook/squangle/archive/8468f07fcc8d96b4af69f1c8b75d404458f8e6b4.tar.gz
Source13  : https://github.com/facebook/wangle/archive/34a04f01668ae88f0dd7ca18aedf50e41689e8f9.tar.gz
Source14  : https://github.com/google/brotli/archive/98ed7a23a83d64133b0a36a884e489bffb0eb864.tar.gz
Source15  : https://github.com/google/double-conversion/archive/f1b955eee1cb94c51074878264aecdd6ee1350dd.tar.gz
Source16  : https://github.com/google/re2/archive/718df09610fee584c9038d8d519697e507e09c9b.tar.gz
Source17  : https://github.com/hhvm/hhvm-third-party/archive/5b6b32f9ae874f280b38dcc3a8e737e1e606a447.tar.gz
Source18  : https://github.com/nih-at/libzip/archive/1d8b1ac4d20b8ef8d3f5d496dabebaa0ff9019ff.tar.gz
Summary  : RPC and serialization framework
Group    : Development/Tools
License  : Apache-2.0 Artistic-1.0 BSD-2-Clause BSD-3-Clause BSD-3-Clause-Attribution BSD-3-Clause-Clear CC-BY-SA-2.0 GPL-2.0 LGPL-2.0 LGPL-2.1 MIT OpenSSL PHP-3.01 Zend-2.0 Zlib bzip2-1.0.6
Requires: hhvm-bin
Requires: hhvm-data
BuildRequires : boost-dev
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : double-conversion-dev
BuildRequires : e2fsprogs-dev
BuildRequires : elfutils-dev
BuildRequires : freetype-dev
BuildRequires : glog-dev
BuildRequires : gmp-dev
BuildRequires : gperf
BuildRequires : icu4c-dev
BuildRequires : jemalloc-dev
BuildRequires : krb5-dev
BuildRequires : libcap-dev
BuildRequires : libdwarf-dev
BuildRequires : libevent-dev
BuildRequires : libmemcached-dev
BuildRequires : libxml2-dev
BuildRequires : lz4-dev
BuildRequires : ncurses-dev
BuildRequires : ocaml
BuildRequires : ocamlbuild
BuildRequires : onig-dev
BuildRequires : openldap-dev
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pcre-dev
BuildRequires : pip
BuildRequires : pkgconfig(Wand)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(libxslt)
BuildRequires : pkgconfig(valgrind)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : scons
BuildRequires : setuptools
BuildRequires : tbb-dev
# Suppress stripping binaries
%define __strip /usr/bin/eu-strip -S
%define debug_package %{nil}
Patch1: 0001-fix_70932.patch
Patch2: 0002-Work-around-gcc-compiler-bug.patch
Patch3: 0003-Ocaml-compatability.patch
Patch4: 0004-Build-break-typing.ml-remove-unused-module.patch
Patch5: 0005-Build-Break-typing.ml-remove-unused-module.patch
Patch6: 0006-Build-break-typing_env.ml-remove-unused-modules.patch
Patch7: 0007-build-fix-ignore-logical-or-errors.patch
Patch8: 0008-Disable-RC4-algorithm-fallback-for-signature-checks.patch
Patch9: 0009-ocaml-ignore-warn_err.patch

%description
Thrift is a software framework for scalable cross-language services
development. It combines a powerful software stack with a code generation
engine to build services that work efficiently and seamlessly between C++,
Java, C#, Python, Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang,
Objective Caml, and Haskell.

%package bin
Summary: bin components for the hhvm package.
Group: Binaries
Requires: hhvm-data

%description bin
bin components for the hhvm package.


%package data
Summary: data components for the hhvm package.
Group: Data

%description data
data components for the hhvm package.


%package dev
Summary: dev components for the hhvm package.
Group: Development
Requires: hhvm-bin
Requires: hhvm-data
Provides: hhvm-devel

%description dev
dev components for the hhvm package.


%prep
tar -xf %{SOURCE17}
tar -xf %{SOURCE14}
tar -xf %{SOURCE2}
tar -xf %{SOURCE15}
tar -xf %{SOURCE3}
tar -xf %{SOURCE4}
tar -xf %{SOURCE6}
tar -xf %{SOURCE7}
tar -xf %{SOURCE18}
tar -xf %{SOURCE1}
tar -xf %{SOURCE8}
tar -xf %{SOURCE10}
tar -xf %{SOURCE16}
tar -xf %{SOURCE12}
tar -xf %{SOURCE5}
tar -xf %{SOURCE13}
tar -xf %{SOURCE9}
tar -xf %{SOURCE11}
cd ..
%setup -q -n hhvm-HHVM-3.17.2
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party
mv %{_topdir}/BUILD/hhvm-third-party-5b6b32f9ae874f280b38dcc3a8e737e1e606a447/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/brotli/src
mv %{_topdir}/BUILD/brotli-98ed7a23a83d64133b0a36a884e489bffb0eb864/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/brotli/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/brotli/src/terryfy
mv %{_topdir}/BUILD/terryfy-8bb673f4410819df06920fdcfd24e18d235d84f7/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/brotli/src/terryfy
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/double-conversion
mv %{_topdir}/BUILD/double-conversion-f1b955eee1cb94c51074878264aecdd6ee1350dd/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/double-conversion
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/fastlz/src
mv %{_topdir}/BUILD/FastLZ-f1217348a868bdb9ee0730244475aee05ab329c5/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/fastlz/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/fatal
mv %{_topdir}/BUILD/fatal-e21df038e0b58855ef9344d1a3a4389e03ba2cc7/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/fatal
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/folly/src
mv %{_topdir}/BUILD/folly-1d2d4f326acc0825690c151c38ac92d146b78146/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/folly/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/libafdt/src
mv %{_topdir}/BUILD/libafdt-eb021a100e761616b35ad62c910d6c336e0711d2/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/libafdt/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/libzip/src
mv %{_topdir}/BUILD/libzip-1d8b1ac4d20b8ef8d3f5d496dabebaa0ff9019ff/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/libzip/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/lz4/src
mv %{_topdir}/BUILD/lz4-d86dc916771c126afb797637dda9f6421c0cb998/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/lz4/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/mcrouter/src
mv %{_topdir}/BUILD/mcrouter-dbf8878c0136e5f94e4bb0aef6f931d5aecfa74d/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/mcrouter/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/proxygen/src
mv %{_topdir}/BUILD/proxygen-e3cdcb4db98d819465af487e9404a8a1032c2300/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/proxygen/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/re2/src
mv %{_topdir}/BUILD/re2-718df09610fee584c9038d8d519697e507e09c9b/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/re2/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/squangle/src
mv %{_topdir}/BUILD/squangle-8468f07fcc8d96b4af69f1c8b75d404458f8e6b4/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/squangle/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/thrift/src
mv %{_topdir}/BUILD/fbthrift-5e5773be567eeb53a75565a911ece7de2c89ee2b/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/thrift/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/wangle/src
mv %{_topdir}/BUILD/wangle-34a04f01668ae88f0dd7ca18aedf50e41689e8f9/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/wangle/src
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/webscalesqlclient/mysql-5.6
mv %{_topdir}/BUILD/mysql-5.6-a9e580b5a0baa768210ef10544c8fab52003ec0b/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/webscalesqlclient/mysql-5.6
mkdir -p %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/webscalesqlclient/mysql-5.6/rocksdb
mv %{_topdir}/BUILD/rocksdb-dcc898b0215cee3b1baa88149c1f39e37e9bfd09/* %{_topdir}/BUILD/hhvm-HHVM-3.17.2/third-party/webscalesqlclient/mysql-5.6/rocksdb
%patch1 -p1
##%patch2 -p1
##%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
##%patch9 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485903145
mkdir clr-build
pushd clr-build
CXXFLAGS=${CXXFLAGS// -Wl,--copy-dt-needed-entries/}
CFLAGS=${CFLAGS// -Wl,--copy-dt-needed-entries/}
export CFLAGS="$CFLAGS -std=gnu++98 "
export FCFLAGS="$CFLAGS -std=gnu++98 "
export FFLAGS="$CFLAGS -std=gnu++98 "
export CXXFLAGS="$CXXFLAGS -std=gnu++98 "
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=/usr/lib64 -Wno-dev -DMYSQL_UNIX_SOCK_ADDR=/run/mariadb/mariadb.sock -DENABLE_ZEND_COMPAT=FALSE -DENABLE_EXTENSION_MCRYPT:BOOL=OFF
make VERBOSE=1 %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1485903145
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/hhvm/CMake/*
/usr/lib64/hhvm/gdb/*
/usr/lib64/hhvm/hphpize/hphpize.cmake
/usr/lib64/hhvm/hphpize/run

%files bin
%defattr(-,root,root,-)
/usr/bin/h2tp
/usr/bin/hh_client
/usr/bin/hh_format
/usr/bin/hh_server
/usr/bin/hhvm
/usr/bin/hhvm-gdb
/usr/bin/hhvm-repo-mode
/usr/bin/hphpize

%files data
%defattr(-,root,root,-)
/usr/share/hhvm/*

%files dev
%defattr(-,root,root,-)
/usr/include/hphp/*
