
PROJECT = anglecalculator
PACKAGE = html


EXPORT_PACKAGE_DATA_DIRS = \
	images \
	css \
	javascripts \


#--------------------------------------------------------------------------
#

all: export-package-data make-cgi-bin-link
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


#--------------------------------------------------------------------------
#
# export
export-package-data: export-package-data-dirs export-package-data-files

include luban/default.def

RSYNC_A = rsync -a --copy-unsafe-links

make-cgi-bin-link:
	cd $(EXPORT_PACKAGE_DIR) && ln -s ../cgi-bin