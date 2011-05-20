# -*- Makefile -*-

PROJECT = chart

# directory structure

RECURSE_DIRS = \
	bin \
	cgi-bin \
	log \
	chart \
	content \
	html \
	config



#--------------------------------------------------------------------------
#

all: 
	BLD_ACTION="all" $(MM) recurse

