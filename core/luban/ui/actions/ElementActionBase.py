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


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from .Action import Action as base, Meta as metabase
class Meta(metabase):

    
    def __new__(cls, name, *args, **kwds):
        # call super class to construct the class
        if py_major_ver == 2:
            target = metabase.__new__(cls, name, *args, **kwds)
        elif py_major_ver == 3:
            target = super().__new__(cls, name, *args, **kwds)
        
        from .exceptions import ElementActionMissingFactoryMethod
        target.ElementActionMissingFactoryMethod = ElementActionMissingFactoryMethod

        # 
        if not target.abstract and target.factory_method is None:
            m = "{!r} is missing class attribute 'factory_method'".format(target)
            raise ElementActionMissingFactoryMethod(m)

        #
        from ._element_action_registry import register
        register(target)
        
        return target
        

# this works for both python 2 and 3
b = Meta('ElementActionBaseBase', (base,), {'abstract': True})
class ElementActionBase(b):
    
    """base class of all actions working on an element
    """

    # decorations
    # .. this is a base class, not a real luban type
    abstract = True
    # .. type of the element this action can work on
    element_type = None # subclass could override this. None means any element
    # .. name of the element action factory method 
    factory_method = None # subclass must override this.

    # attributes
    # .. element action always works on a selected element
    element = descriptors.action() # action to select an element

    # exceptions
    from .exceptions import ActionFactoryMethodConflict

    # helper method for subclasses
    def _elementSelector(self, element):
        """create element selector for the given element
        """
        from ..elements.Element import Element
        if isinstance(element, Element):
            from . import select
            return select(element=element)
        
        from .ActionBase import ActionBase
        if isinstance(element, ActionBase):
            return element
        raise NotImplementedError


    def __init__(self, element=None, **kwds):
        self.element = self._elementSelector(element)
        if py_major_ver == 2:
            super(ElementActionBase, self).__init__(**kwds)
        elif py_major_ver == 3:
            super().__init__(**kwds)
        return


# End of file 

