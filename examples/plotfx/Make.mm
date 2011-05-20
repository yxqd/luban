# -*- Makefile -*-

PROJECT = plotfx

# directory structure

RECURSE_DIRS = \
	bin \
	cgi-bin \
	plotfx \
	config \


INIT_MUTABLE_DATA_DIRS = \
	content/data \
	log \


EXPORT_PACKAGE_DATA_DIRS = \
	content \
	html \
	plotfx \

#--------------------------------------------------------------------------
#

all: export-package-data-dirs init-mutable-data-dirs
	BLD_ACTION="all" $(MM) recurse


#
include luban/default.def
RSYNC_A = rsync -a --copy-unsafe-links

