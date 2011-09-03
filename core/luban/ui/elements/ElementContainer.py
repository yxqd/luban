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
class ElementContainer(Element, metaclass=Meta):

    """base class of element container types

    Usually one should not subclass this class directly 
    to create new types of element containers. 
    One should subclass either SimpleContainer.SimpleContainer
    or Riveted.RivetedContainer.
    """

    # decorations
    abstract = True


    # exceptions
    class ElementDefinitionError(Exception): pass
    class SubelementDisallowedError(Exception): pass


    # attributes
    contents = descriptors.object(default=[])
    contents.tip = 'sub elements'

    
    # methods
    def append(self, item):
        """append the given subelement to my contents
        """
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


    def getChildByName(self, name):
        """get one of my children by his name
        """
        return self.name2item[name]


    def getDescendentByID(self, id):
        """get a descendent by its id
        """
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


    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.name2item = {}
        self.id2item = {}
        self.contents = []
        return


    # implementation details
    @classmethod
    def _isAllowedSubElement(cls, type):
        """check whether the given element type 
        can be a subelement of this element type.
        """
        if cls.child_types != 'any' and type not in cls.child_types:
            return False
            
        if type.parent_types is None:
            return False
        
        if type.parent_types == 'any':
            return True

        # 
        for t in type.parent_types:
            if cls is t:
                return True
        return False

    
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
