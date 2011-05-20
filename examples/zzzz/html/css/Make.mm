# -*- Makefile -*-

PROJECT = zzzz
PACKAGE = html/css

RECURSE_DIRS = \

EXPORT_PACKAGE_DATA_DIRS = \
	jquery\
	luban\
	skeleton\
	tabulator\
	other\


EXPORT_PACKAGE_DATA_FILES = \
	luban.css\


OTHERS = \

#--------------------------------------------------------------------------
#

all: export-package-data
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse



#
include luban/default.def

RSYNC_A = rsync -a --copy-unsafe-links

export-package-data: export-package-data-dirs export-package-data-files


# version
# $Id$

# End of file
