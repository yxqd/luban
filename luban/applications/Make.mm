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
PACKAGE = applications


# directory structure

BUILD_DIRS = \

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
	CGIInputCollector.py \
	CGIParser.py \
	CliApplication.py \
	CreateLubanProject.py \
	DownloadLubanProject.py \
	LaunchDetached.py \
	ProjectScriptBase.py \
	SimpleHttpServer.py \
	SimpleHttpServerDaemon.py \
	SSHTunnel.py \
	StartLubanProject.py \
	StopLubanProject.py \
	SuperApp.py \
	SuperAppBase.py \
	SuperAppForDaemon.py \
	Timer.py \
	UIApp.py \
	WebApplication.py \
	WXApplication.py \
	__init__.py \
	configurationSaver.py \
	utils.py \



#include doxygen/default.def

export:: export-package-python-modules 


docs: export-doxygen-docs

# version
# $Id: Make.mm 1213 2006-11-18 16:17:08Z linjiao $

# End of file
