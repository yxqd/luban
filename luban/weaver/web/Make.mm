# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin    
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = luban
PACKAGE = weaver/web


# directory structure

BUILD_DIRS = \
	content \
	libraries \
	weaver \
	_json \


OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	DocumentMill.py \
	HtmlMill.py \
	Librarian.py \
	__init__.py \
	_utils.py \



EXPORT_PACKAGE_DATA_DIRS = \
	css \
	javascripts \



#include doxygen/default.def


export:: export-package-python-modules export-package-data-dirs


RSYNC_A = rsync -a
export-package-data-dirs::
	for x in $(EXPORT_PACKAGE_DATA_DIRS); do { \
            if [ -d $$x ]; then { \
                $(RSYNC_A) $$x/ $(EXPORT_MODULEDIR)/$(PACKAGE)/$$x/; \
            } fi; \
        } done


docs: export-doxygen-docs

# version
# $Id: Make.mm 1213 2006-11-18 16:17:08Z linjiao $

# End of file
