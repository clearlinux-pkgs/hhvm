PKG_NAME := hhvm
URL := https://github.com/facebook/hhvm/archive/HHVM-3.17.2.tar.gz
ARCHIVES := https://github.com/hhvm/hhvm-third-party/archive/5b6b32f9ae874f280b38dcc3a8e737e1e606a447.tar.gz third-party \
	https://github.com/google/brotli/archive/98ed7a23a83d64133b0a36a884e489bffb0eb864.tar.gz third-party/brotli/src \
	https://github.com/MacPython/terryfy/archive/8bb673f4410819df06920fdcfd24e18d235d84f7.tar.gz third-party/brotli/src/terryfy \
	https://github.com/google/double-conversion/archive/f1b955eee1cb94c51074878264aecdd6ee1350dd.tar.gz third-party/double-conversion \
	https://github.com/ariya/FastLZ/archive/f1217348a868bdb9ee0730244475aee05ab329c5.tar.gz third-party/fastlz/src \
	https://github.com/facebook/fatal/archive/e21df038e0b58855ef9344d1a3a4389e03ba2cc7.tar.gz third-party/fatal \
	https://github.com/facebook/folly/archive/1d2d4f326acc0825690c151c38ac92d146b78146.tar.gz third-party/folly/src \
	https://github.com/facebook/libafdt/archive/eb021a100e761616b35ad62c910d6c336e0711d2.tar.gz third-party/libafdt/src \
	https://github.com/nih-at/libzip/archive/1d8b1ac4d20b8ef8d3f5d496dabebaa0ff9019ff.tar.gz third-party/libzip/src \
	https://github.com/Cyan4973/lz4/archive/d86dc916771c126afb797637dda9f6421c0cb998.tar.gz third-party/lz4/src \
	https://github.com/facebook/mcrouter/archive/dbf8878c0136e5f94e4bb0aef6f931d5aecfa74d.tar.gz third-party/mcrouter/src \
	https://github.com/facebook/proxygen/archive/e3cdcb4db98d819465af487e9404a8a1032c2300.tar.gz third-party/proxygen/src \
	https://github.com/google/re2/archive/718df09610fee584c9038d8d519697e507e09c9b.tar.gz third-party/re2/src \
	https://github.com/facebook/squangle/archive/8468f07fcc8d96b4af69f1c8b75d404458f8e6b4.tar.gz third-party/squangle/src \
	https://github.com/facebook/fbthrift/archive/5e5773be567eeb53a75565a911ece7de2c89ee2b.tar.gz third-party/thrift/src \
	https://github.com/facebook/wangle/archive/34a04f01668ae88f0dd7ca18aedf50e41689e8f9.tar.gz third-party/wangle/src \
	https://github.com/facebook/mysql-5.6/archive/a9e580b5a0baa768210ef10544c8fab52003ec0b.tar.gz third-party/webscalesqlclient/mysql-5.6 \
	https://github.com/facebook/rocksdb/archive/dcc898b0215cee3b1baa88149c1f39e37e9bfd09.tar.gz third-party/webscalesqlclient/mysql-5.6/rocksdb

include ../common/Makefile.common
