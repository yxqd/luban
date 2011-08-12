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


# insert a new element before an element


class InsertBeforeElement(base):

    abstract = False

    def identify(self, inspector):
        return inspector.onInsertElement(self)
    

    element = descriptors.action()
    newelement = descriptors.element()

    
    def __init__(self, element=None, newelement=None):
        '''insert newelement 

        element: the element of reference
        newelement: new ui element to insert, can be anything like document etc
        '''
        super(InsertBeforeElement, self).__init__()
        self.newelement = newelement
        self.element = self._elementSelector(element)
        return


# version
__id__ = "$Id$"

# End of file 

