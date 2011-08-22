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



from .AttributeContainer import AttributeContainer, Meta
class ActionBase(AttributeContainer):

    """base class of all actions
    """

    # decorations
    abstract = True

    # don't override this
    lubanaction = descriptors.bool(default=True)

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
        if isinstance(element, ActionBase):
            return element
        raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 
