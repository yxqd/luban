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


PROJECT = sansmodel

# directory structure

RECURSE_DIRS = \
	bin \
	cgi-bin \
	sansmodel \
	content \
	html \
	config


INIT_MUTABLE_DATA_DIRS = \
	content/data \
	log \


#--------------------------------------------------------------------------
#

all: init-mutable-data-dirs
	BLD_ACTION="all" $(MM) recurse


include luban/default.def


# version
# $Id$

# End of file
