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



from .AttributeContainer import AttributeContainer
class Action(AttributeContainer):

    # base class of all actions
    
    abstract = True
    
    callback = descriptors.reference(name='callback')
    callback.experimental = True
    callback.tip = 'A callback action that will be performed when the current action is finished'
    

    def identify(self, inspector):
        raise NotImplementedError("class %r should implement 'identify'" % self.__class__.__name__)


    def __init__(self, name=None, **kwds):
        AttributeContainer.__init__(self)
        
        self.name = name

        for k, v in kwds.items():
            self.setAttribute(k,v)

        return


    def elementSelector(self, element):
        """create element selector for the given element
        """
        from ..elements.Element import Element
        if isinstance(element, Element):
            from .SelectByElement import SelectByElement
            return SelectByElement(element)
        if isinstance(element, Action):
            return element
        raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 
