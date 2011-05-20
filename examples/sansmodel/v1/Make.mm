
PROJECT = sansmodel

# directory structure

RECURSE_DIRS = \
	bin \
	cgi-bin \
	log \
	content \
	html \
	sansmodel \
	config



#--------------------------------------------------------------------------
#

all: 
	BLD_ACTION="all" $(MM) recurse

