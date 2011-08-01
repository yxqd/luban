#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .Panel import Panel
from .CommonInterface import CommonInterface

class TreeViewContainer(Panel, CommonInterface):


    def __getattr__(self, name):
        return getattr(self.tree, name)

    
    def select(self, node=None):
        return self.tree.select(node=node)


    def removeNode(self, node=None):
        return self.tree.removeNode(node=node)
        
    
    pass # end of Panel



# version
__id__ = "$Id$"

# End of file 
