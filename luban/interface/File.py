#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                     (C) 2009-2010  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# this is not really a UI element
# it represents the file offered by controller (server)
# to be downloaded.

from luban.content.ElementContainer import ElementContainer as base

class File(base):

    def identify(self, visitor):
        return visitor.onFile(self)

    filename = base.descriptors.str('filename')
    content = base.descriptors.str('content')
    

# version
__id__ = "$Id$"

# End of file 
