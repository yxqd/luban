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


## create Make.mm for recursing into subdirs


template = r'''# -*- Makefile -*-

PROJECT = %(project)s

# directory structure

RECURSE_DIRS = \
%(subdirs)s


#--------------------------------------------------------------------------
#

all: 
	BLD_ACTION="all" $(MM) recurse

''' 


class Generator:

    def __init__(self, project, subdirs):
        """Generator( 'mcstas2', ['a', 'b'] )
        """
        self.project = project
        self.subdirs = subdirs
        return
    
    def generate(self):

        subdirs_str = '\t' + (' \\'+'\n\t').join( self.subdirs ) + '\n'
        project_str = self.project
        
        content = template % {
            'subdirs' : subdirs_str,
            'project': project_str,
            }
        
        return content

    pass # end of Generate


# version
__id__ = "$Id$"

# End of file 
