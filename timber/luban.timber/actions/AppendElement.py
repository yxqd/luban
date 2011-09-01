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


from .Action import Action as base

class AppendElement(base):

    abstract = False

    def identify(self, inspector):
        return inspector.onAppendElement(self)
    

    element = descriptors.element() 
    container = descriptors.action() # must be an action to select an element

    
    def __init__(self, element=None, container=None):
        '''append an element to a container

        element: the element to be appended. 
        container: the container to which the element will be appended.
        '''
        super(AppendElement, self).__init__()
        self.element = element
        self.container = self._elementSelector(container)
        return


# version
__id__ = "$Id$"

# End of file 

