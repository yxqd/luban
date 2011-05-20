# -*- Makefile -*-

PROJECT = sansmodel
PACKAGE = content

#--------------------------------------------------------------------------
#

all: export-package-data-dirs
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PACKAGE_DATA_DIRS = \
	components \
	images \


include luban/default.def
