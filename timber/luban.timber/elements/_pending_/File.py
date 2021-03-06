#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                     (C) 2011-2010  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# this is not really a UI element
# it represents the file offered by controller (server)
# to be downloaded.

from luban.ui.elements.ElementContainer import ElementContainer as base

class File(base):

    def identify(self, visitor):
        return visitor.onFile(self)

    filename = descriptors.str('filename')
    content = descriptors.str('content')
    

# version
__id__ = "$Id$"

# End of file 
