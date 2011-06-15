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
    

    element = descriptors.reference()
    container = descriptors.reference()

    
    def __init__(self, element=None, container=None):
        '''append an element to a container

        element: the element to be appended. please note that it is not a hierarchy.
            It is just a single node.
        container: the action to select the container to which the element will be
            appended.
        '''
        super(AppendElement, self).__init__()
        self.element = element
        self.container = self.elementSelector(container)
        return


# version
__id__ = "$Id$"

# End of file 

