# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## create Make.mm for exporting data dir


template = r'''# -*- Makefile -*-

PROJECT = %(project)s
PACKAGE = %(package)s

#--------------------------------------------------------------------------
#

all: export-data-files
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

EXPORT_DATAFILES = \
%(datafiles)s


CP_F = rsync -r --copy-unsafe-links --links
EXPORT_DATA_PATH = $(EXPORT_ROOT)/$(PROJECT)/$(PACKAGE)

export-data-files::
	mkdir -p $(EXPORT_DATA_PATH); \
	for x in $(EXPORT_DATAFILES); do { \
	  $(CP_F) $$x $(EXPORT_DATA_PATH)/ ; \
	} done

''' 


class Generator:

    target = 'Make.mm'

    def __init__(self, project, package, datafiles):
        """Generator( 'project', 'package', ['a', 'b'])
        """
        self.project = project
        self.package = package
        self.datafiles = datafiles
        return
    
    def generate(self):
        '''generate( "/path/to/somewhere", "pythonpackage.mk" )
        '''
        datafiles_str = '\t' + (' \\'+'\n\t').join( self.datafiles ) + '\n'
        package_str = self.package
        content = template % {
            'datafiles' : datafiles_str,
            'package' : package_str,
            'project': self.project,
            }
        return content

    pass # end of Generate


def test():
    generator = Generator('project', 'package', ['a', 'b', 'c'])
    print generator.generate()
    return

if __name__=='__main__': test()


# version
__id__ = "$Id$"

# End of file 
