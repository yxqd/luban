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


from ..meta.TypeRegistryCurator import registry
from .ElementBase import ElementBase
from .Element import Element


# public interface
element_types = None


# implementations
# proxy that looks like a registry of element types
class ElementTypes:


    def __init__(self):
        global registry
        self.registry = registry
        self.names = [] # names of element types
        return


    def getElementClass(self, name):
        k = self.registry.get(name)
        if k is None:
            return
        if not issubclass(k, ElementBase):
            return
        return k

    
    def types(self):
        all_types = self.registry.types()
        for t in all_types:
            if issubclass(t, Element):
                yield t
        return


    def onRegistration(self, cls):
        from .. import e
        if issubclass(cls, ElementBase):
            self.names.append(cls.__unique_type_name__)
        return


element_types = ElementTypes()
registry.observers.append(element_types)


# End of file 
