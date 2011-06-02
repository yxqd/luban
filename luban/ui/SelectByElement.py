# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from ElementActions import ElementActions
from Action import Action as base

class SelectByElement(ElementActions, base):


    abstract = False


    def identify(self, inspector):
        return inspector.onSelectByElement(self)


    def getElementType(self):
        return self.element.__class__.__name__
    

    element = base.descriptors.reference(name='element')
    
    def __init__(self, element=None):
        base.__init__(self, name='selectbyelement')
        self.element = element
        return


# version
__id__ = "$Id$"

# End of file 

