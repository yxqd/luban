# -*- Makefile -*-

PROJECT = sansmodel
PACKAGE = config

#--------------------------------------------------------------------------
#

all: export-package-data-files init-package-data-files
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

EXPORT_PACKAGE_DATA_FILES = \
	SimpleHttpServer.pml \
	journal.pml \
	librarian.pml \
	main.pml \
	widget.lib



INIT_PACKAGE_DATA_FILES = \
	clerk.pml \
	guid.pml \
	web-weaver.pml \


include luban/default.def
