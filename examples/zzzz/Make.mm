# -*- Makefile -*-

PROJECT = zzzz

# directory structure

RECURSE_DIRS = \
	bin \
	cgi-bin \
	log \
	zzzz \
	content \
	html \
	config



#--------------------------------------------------------------------------
#

all: 
	BLD_ACTION="all" $(MM) recurse

