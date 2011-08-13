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


from .Action import Action as base, Meta
class ElementActionBase(base, metaclass=Meta):
    
    """base class of all actions working on an element
    """
    
    abstract = True

    # attributes
    # .. element action always works on a selected element
    element = descriptors.action() # action to select an element


    def __init__(self, element=None, **kwds):
        self.element = self._elementSelector(element)
        super().__init__(**kwds)
        return


# End of file 

