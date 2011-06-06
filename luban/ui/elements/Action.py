#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao  Lin
#                      California Institute of Technology
#                      (C) 2005-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# base class of all actions

from .AttributeContainer import AttributeContainer
from pyre.parsing.locators.Traceable import Traceable

class Action(AttributeContainer, Traceable):

    abstract = True
    
    callback = descriptors.reference(name='callback')
    callback.experimental = True
    callback.tip = 'A callback action that will be performed when the current action is finished'
    

    def identify(self, inspector):
        raise NotImplementedError("class %r should implement 'identify'" % self.__class__.__name__)


    def __init__(self, name=None, **kwds):
        Traceable.__init__(self)

        # name should be unecessary. this is due to the implementation limit of AttributeContainer class
        name = name or (self.__class__.__name__ + str(id(self)) )

        # this should not be necessary if we are not using pyre Inventory
        # to implement AttributeContainer
        AttributeContainer.__init__(self, name)
        self.name = name

        for k, v in kwds.items():
            self.setAttribute(k,v)

        return


    def elementSelector(self, element):
        # factory to select an element
        from .Element import Element
        if isinstance(element, Element):
            from .SelectByElement import SelectByElement
            return SelectByElement(element)
        if isinstance(element, Action):
            return element
        raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 
