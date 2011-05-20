
PROJECT = anglecalculator

# directory structure

RECURSE_DIRS = \
	bin \
	cgi-bin \
	log \
	anglecalculator \
	content \
	html \
	config



#--------------------------------------------------------------------------
#

all: 
	BLD_ACTION="all" $(MM) recurse

