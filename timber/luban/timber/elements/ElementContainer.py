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


from .Element import Element, Meta
from .CredentialFactory import CredentialFactory
class ElementContainer(CredentialFactory, Element, metaclass=Meta):


    class ElementDefinitionError(Exception): pass
    class SubelementDisallowedError(Exception): pass


    #
    contents = descriptors.object(default=[])
    contents.tip = 'sub elements'

    
    # this helps establish the context in which derived element types
    # would be defined. see ..AttributeContainer.Meta for more details
    @classmethod
    def __get_subclass_preparation_context__(cls):
        d = super().__get_subclass_preparation_context__()
        from .UIElementFacilityMapping import UIElementFacilityMapping
        m = UIElementFacilityMapping('all')
        from . import _registry
        reg = _registry.fundamental_elements
        names = reg.names()
        for name in names:
            ecls = reg.getElementClass(name)
            if not ecls.abstract and cls._isAllowedSubElement(ecls):
                d[name] = m[name]
            continue
        return d
    

    def append(self, item):
        # if it is a piece of text, just add it
        if isinstance(item, str):
            self.contents.append(item)
            return self
        
        # check item name
        if item.name in self.name2item:
            e = 'item of same name has been added, please consider change the name. name=%r, item=%s' \
                % (item.name, item)
            raise RuntimeError(e)

        # check item type
        self._checkSubElementType(item)
        
        # append
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
    

    @classmethod
    def _isAllowedSubElement(cls, type):
        if hasattr(cls, 'allowed_element_types') and hasattr(cls, 'disallowed_element_types'):
            raise cls.ElementDefinitionError("an element type cannot have both allowed_element_types and disallowed_element_types")
        
        if hasattr(cls, 'allowed_element_types'):
            allowed = cls.allowed_element_types
            for t in allowed:
                # this line seems redundant but let us keep it here just
                # in case python behaviour of issubclass changed
                if type is t: return True
                if issubclass(type, t): return True
                continue
            return False
        
        if hasattr(cls, 'disallowed_element_types'):
            disallowed = cls.disallowed_element_types
            for t in disallowed:
                if type is t: return False
                if issubclass(type, t): return False
                continue
            return True
            
        return True

    
    def _checkSubElementType(self, subelem):
        """check the type of the sub element to make sure 
        it can be appended into this element
        """
        
        #
        cls = self.__class__
        
        if self.__class__._isAllowedSubElement(subelem.__class__):
            return


        # compose error message
        msg = 'element %s is not allowed to be subelement of %s. '\
            % (subelem.__class__.__name__, cls.__name__,)

        #
        allowed = getattr(cls, 'allowed_element_types', None)
        if allowed:
            msg += 'allowed element types are %s' % ','.join(t.__name__ for t in allowed)

        #
        disallowed = getattr(cls, 'disallowed_element_types', None)
        if disallowed:
            msg += 'dis-allowed element types are %s' % ','.join(
                t.__name__ for t in disallowed)
        
        #
        raise cls.SubelementDisallowedError(msg)
            

    def __init__(self, **kwds):
        super().__init__(**kwds)
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