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


# replace an element with a new element


class ReplaceElement(base):

    abstract = False

    def identify(self, inspector):
        return inspector.onReplaceElement(self)
    

    element = base.descriptors.reference(name='element')
    newelement = base.descriptors.reference(name='newelement')

    
    def __init__(self, element=None, newelement=None):
        '''insert newelement 

        element: the element to be replaced
        newelement: new ui element, can be anything like document etc
        '''
        super(ReplaceElement, self).__init__()
        self.newelement = newelement
        self.element = self.elementSelector(element)
        return


# version
__id__ = "$Id$"

# End of file 

