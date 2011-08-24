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


from .Action import Action as base, Meta as metabase


class Meta(metabase):

    
    def __new__(cls, name, *args, **kwds):
        # call super class to construct the class
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
        


class ElementActionBase(base, metaclass=Meta):
    
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

    def __init__(self, element=None, **kwds):
        self.element = self._elementSelector(element)
        super().__init__(**kwds)
        return


# End of file 
