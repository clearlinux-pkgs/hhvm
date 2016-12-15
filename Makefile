PKG_NAME := hhvm
URL := https://github.com/facebook/hhvm/archive/HHVM-3.15.0.tar.gz
ARCHIVES := https://github.com/hhvm/hhvm-third-party/archive/415fe3a6cb677d2e13acd8d0c8456672ef13f340.tar.gz third-party \
	https://github.com/google/brotli/archive/98ed7a23a83d64133b0a36a884e489bffb0eb864.tar.gz third-party/brotli/src \
	https://github.com/MacPython/terryfy/archive/8bb673f4410819df06920fdcfd24e18d235d84f7.tar.gz third-party/brotli/src/terryfy \
	https://github.com/google/double-conversion/archive/f1b955eee1cb94c51074878264aecdd6ee1350dd.tar.gz third-party/double-conversion \
	https://github.com/ariya/FastLZ/archive/f1217348a868bdb9ee0730244475aee05ab329c5.tar.gz third-party/fastlz/src \
	https://github.com/facebook/fatal/archive/dc8cac9aa5f3c7599b24854048536a62da88a2f1.tar.gz third-party/fatal \
	https://github.com/facebook/folly/archive/6a7f9395dde570c8dc01ef489da9185170c52385.tar.gz third-party/folly/src \
	https://github.com/facebook/libafdt/archive/eb021a100e761616b35ad62c910d6c336e0711d2.tar.gz third-party/libafdt/src \
	https://github.com/nih-at/libzip/archive/1d8b1ac4d20b8ef8d3f5d496dabebaa0ff9019ff.tar.gz third-party/libzip/src \
	https://github.com/Cyan4973/lz4/archive/d86dc916771c126afb797637dda9f6421c0cb998.tar.gz third-party/lz4/src \
	https://github.com/facebook/mcrouter/archive/6aff7f07f69e851d78102141b96d169c565bf086.tar.gz third-party/mcrouter/src \
	https://github.com/facebook/proxygen/archive/fab05a83c68dd9752ca46d722f4b3da836155191.tar.gz third-party/proxygen/src \
	https://github.com/google/re2/archive/718df09610fee584c9038d8d519697e507e09c9b.tar.gz third-party/re2/src \
	https://github.com/facebook/squangle/archive/4ec32a3ce547f25cd9637263e5f30d7bf3eabcf3.tar.gz third-party/squangle/src \
	https://github.com/facebook/fbthrift/archive/ced32d089f642019a859bb8d39e85d38cab3c607.tar.gz third-party/thrift/src \
	https://github.com/facebook/wangle/archive/ae57c480ca5934e6279e9086f98f207fde2f5355.tar.gz third-party/wangle/src \
	https://github.com/facebook/mysql-5.6/archive/a9e580b5a0baa768210ef10544c8fab52003ec0b.tar.gz third-party/webscalesqlclient/mysql-5.6 \
	https://github.com/facebook/rocksdb/archive/dcc898b0215cee3b1baa88149c1f39e37e9bfd09.tar.gz third-party/webscalesqlclient/mysql-5.6/rocksdb

include ../common/Makefile.common
