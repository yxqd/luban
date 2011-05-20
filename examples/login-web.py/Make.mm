# -*- Makefile -*-

PROJECT = login-web.py

# directory structure

RECURSE_DIRS = \


INIT_MUTABLE_DATA_DIRS = \


EXPORT_PACKAGE_DATA_DIRS = \
	static \


EXPORT_PACKAGE_DATA_FILES = \
	README \
	server.py \

#--------------------------------------------------------------------------
#

all: export-package-data-dirs export-package-data-files init-mutable-data-dirs
	BLD_ACTION="all" $(MM) recurse


#
include luban/default.def
RSYNC_A = rsync -a --copy-unsafe-links

