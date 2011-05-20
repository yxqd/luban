#!/usr/bin/env python
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


## create Make.mm for exporting python package


template = r'''# -*- Makefile -*-

PROJECT = %(package)s

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
%(modules)s


export:: export-python-modules
''' 


class Generator:

    def __init__(self, package, modules):
        """Generator( 'mcstas2.components.monitors', ['E_monitor.py'] )
        """
        self.package = package
        self.modules = modules
        return
    
    def generate(self):

        modules_str = '\t' + (' \\'+'\n\t').join( self.modules ) + '\n'
        package_str = self.package.replace( '.', '/' )
        
        content = template % {
            'modules' : modules_str,
            'package' : package_str,
            }
        
        return content

    pass # end of Generate


# version
__id__ = "$Id$"

# End of file 
