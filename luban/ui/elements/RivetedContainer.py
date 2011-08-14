#!/usr/bin/env python
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


from .ElementContainer import ElementContainer, Meta

class RivetedContainer(ElementContainer):

    """containier that has specific types of sub elements. 
    For examples, a tabs container will only have tab elements as children.
    """

    pass


class RivetedSubElement:
    
    """mixin class to denote an element is a sub element of a RivetedContainer
    """

    # parent type should be limited to only one type
    # subclass need to overload this
    parent_types = []


# version
__id__ = "$Id$"

# End of file 
