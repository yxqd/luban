
PROJECT = plotfx
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
	guid.pml \
	librarian.pml \
	main.pml \


INIT_PACKAGE_DATA_FILES = \
	SimpleHttpServer.pml \
	clerk.pml \
	journal.pml \
	web-weaver.pml \


include luban/default.def

