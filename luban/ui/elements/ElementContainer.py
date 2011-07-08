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


from .Element import Element
from .CredentialFactory import CredentialFactory
class ElementContainer(Element, CredentialFactory):

    
    @classmethod
    def __get_subclass_preparation_context__(cls):
        d = super().__get_subclass_preparation_context__()
        from .UIElementFacilityMapping import UIElementFacilityMapping
        m = UIElementFacilityMapping('all')
        from . import _registry
        reg = _registry.fundamental_elements
        names = reg.names()
        for name in names:
            cls = reg.getElementClass(name)
            if not cls.abstract:
                d[name] = m[name]
            continue
        return d
    

    def append(self, item):
        if isinstance(item, str):
            self.contents.append(item)
            return self
        
        if item.name in self.name2item:
            e = 'item of same name has been added, please consider change the name: %r(%s)' \
                % (item.name, item)
            raise RuntimeError(e)

        # this should be in the meta class
        if hasattr(self, 'allowed_element_types') and hasattr(self, 'disallowed_element_types'):
            raise RuntimeError("an element type cannot have both allowed_element_types and disallowed_element_types")
        
        if hasattr(self, 'allowed_element_types'):
            allowed = self.allowed_element_types
            good = False
            for t in allowed:
                if isinstance(item, t): good = True; break;
                continue
            if not good:
                raise ValueError('element %s is not allowed to be subelement of %s. allowed element types are %s' % (
                    item.__class__.__name__,
                    self.__class__.__name__,
                    ','.join([t.__name__ for t in allowed]),
                    ))
        if hasattr(self, 'disallowed_element_types'):
            disallowed = self.disallowed_element_types
            good = True
            for t in disallowed:
                if isinstance(item, t): good = False; break;
                continue
            if not good:
                raise ValueError('element %s is not allowed to be subelement of %s. Disallowed element types are %s' % (
                    item.__class__.__name__,
                    self.__class__.__name__,
                    ','.join([t.__name__ for t in disallowed]),
                    ))
            
        self.contents.append(item)
        self._registerChild(item)
        return self


    def add(self, element):
        import warnings
        warnings.warn("method 'add' replaced by 'append'")
        return self.append(element)


    def getChildByName(self, name):
        return self.name2item[name]


    def getDescendentByName(self, name):
        'find a descendent by its name. the name must be unique among descendents'
        if name in self.name2item: return self.name2item[name]
        for item in self.contents:
            if not isContainer(item): continue
            candidate = item.getDescendentByName(name)
            if candidate: return candidate
            continue
        return


    def getDescendentByID(self, id):
        if not self.id2item and self.contents:
            self._registerChildren(self.contents)
        if id in self.id2item: return self.id2item[id]
        for item in self.contents:
            if not isContainer(item): continue
            candidate = item.getDescendentByID(id)
            if candidate: return candidate
            continue
        return


    def find(self, id=None):
        if id:
            return self.getDescendentByID(id)
        raise NotImplementedError


    def __getattr__(self, name):
        return self.getChildByName(name)
    

    def _iterDeclaredSubElements(self):
        from .Element import Element
        for trait in self.pyre_getTraitDescriptors():
            if trait not in self.pyre_inventory:
                continue
            slot = self.pyre_inventory[trait]
            value = slot.value
            if isinstance(value, Element):
                yield value
            continue
        return
    
    
    def __init__(self, **kwds):
        super().__init__(self, **kwds)
        self.name2item = {}
        self.id2item = {}
        self.contents = []
        
        # pyre machinery should be all done here
        # so we should have configured sub elements
        # it should be safe to add sub elements to my store
        for elem in list(self._iterDeclaredSubElements()):
            self.append(elem)
            continue
        return


    def _registerChildren(self, children):
        for child in children:
            self._registerChild(child)
        return


    def _registerChild(self, item):
        self.name2item[item.name] = item
        self.id2item[item.id] = item
        return



def isContainer(candidate):
    return isinstance(candidate, ElementContainer)


# decorator
def elementfactory(method):
    method.iselementfactory = True
    return method


# version
__id__ = "$Id$"

# End of file 
