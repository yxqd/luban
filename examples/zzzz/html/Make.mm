# -*- Makefile -*-

PROJECT = zzzz
PACKAGE = html

RECURSE_DIRS = \
	javascripts \
	css \

EXPORT_PACKAGE_DATA_DIRS = \
	images \

EXPORT_PACKAGE_DATA_FILES = \


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


RSYNC_A = rsync -a
EXPORT_DATA_PATH = $(EXPORT_ROOT)/$(PROJECT)/$(PACKAGE)


export-package-data: export-package-data-dirs export-package-data-files make-cgi-bin-link


make-cgi-bin-link:
	if [ ! -h $(EXPORT_PACKAGE_DIR)/cgi-bin ]; then {\
	  cd $(EXPORT_PACKAGE_DIR) && ln -s ../cgi-bin ; \
	} fi


# version
# $Id$

# End of file
