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

PROJECT = luban-demo1
PACKAGE = config

#--------------------------------------------------------------------------
#

all: export-config-files init-config-files
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


EXPORT_DATAFILES = \
	SimpleHttpServer.pml \
	democlerk.odb \
	democlerk.pml \
	journal.pml \
	librarian.pml \
	main.pml \
	web-weaver-library.pml \
	wx-weaver.pml \


INIT_DATAFILES = \
	web-weaver.pml \



CP_F = cp -f
EXPORT_DATA_PATH = $(EXPORT_ROOT)/$(PROJECT)/$(PACKAGE)

export-config-files:: 
	mkdir -p $(EXPORT_DATA_PATH); \
	for x in $(EXPORT_DATAFILES); do { \
	  $(CP_F) $$x $(EXPORT_DATA_PATH)/ ; \
        } done


# copy the data files over only if they do not exist
init-config-files:
	mkdir -p $(EXPORT_DATA_PATH); \
	for x in $(INIT_DATAFILES); do { \
            if [ -e $$x -a ! -e $(EXPORT_DATA_PATH)/$$x ]; then { \
	        $(CP_F) $$x $(EXPORT_DATA_PATH)/ ; \
            } fi; \
        } done


# version
# $Id: Make.mm,v 1.1.1.1 2006-11-27 00:09:14 aivazis Exp $

# End of file
