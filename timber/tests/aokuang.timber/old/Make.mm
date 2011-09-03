# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin    
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = aokuang
PACKAGE = 

RECURSE_DIRS = \
	content \
	bin \
	cgi-bin \
	html \
	config \

EXPORT_PACKAGE_DATA_DIRS = \
	aokuang

INIT_MUTABLE_DATA_DIRS = \
	log \
	content/data \


OTHERS = \


PROJ_TIDY += svn-commit*.tmp

#--------------------------------------------------------------------------
#

all: export-package-data-dirs init-mutable-data-dirs
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


include luban/default.def


# version
# $Id: Make.mm,v 1.1.1.1 2006-11-27 00:09:14 aivazis Exp $

# End of file
