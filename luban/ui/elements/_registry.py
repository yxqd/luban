# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# public interface
def registerAllElements(package):
    """register all elements in the given package"""
    return package.registerAllElements()

element_types = None


# implementations
# proxy that looks like a registry of element types
class ElementTypes:


    def __init__(self):
        from ..meta.TypeRegistryCurator import registry
        self.registry = registry
        return


    def getElementClass(self, name):
        k = self.registry.get(name)
        if k is None:
            return
        from .ElementBase import ElementBase
        if not issubclass(k, ElementBase):
            return
        return k


element_types = ElementTypes()


# version
__id__ = "$Id$"

# End of file 
