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
def register(cls):
    all_element_classes.append(cls)

    if \
            "__fundamental_element__" in cls.__dict__ and cls.__fundamental_element__ \
            or not hasSubElements(cls):
        
        fundamental_elements.register(cls)
    
    return cls


def registerAllElements(package):
    """register all elements in the given package"""
    return package.registerAllElements()




# implementations

# list of all element classes
all_element_classes = []


# registry of element classes that are "fundamental"
class FundamentalElements:


    def __init__(self):
        self._store = {}
        self._cls2name = {}
        return


    def names(self):
        return self._store.keys()


    def __iter__(self):
        return iter(self._store)


    def register(self, cls):
        name = self._getUniqueName(cls)
        if name in self._store:
            if self._store[name] is cls:
                # already registered
                return
            # conflict
            m = "element type of the same name already registered. name: %s, new element: %s, existing element: %s" % (name, cls, self._store[name])
            raise RuntimeError(m)

        # register
        self._store[name] = cls
        self._cls2name[cls] = name
        return


    def getElementClass(self, name):
        return self._store.get(name)


    def _getUniqueName(self, target):
        # get unique name to identify the element type
        sig  = '__unique_type_name__'
        if hasattr(target, sig):
            name = getattr(target, sig)
        else:
            name = target.__name__
        return name


fundamental_elements = FundamentalElements()


#
def hasSubElements(cls):
    traits = cls.pyre_localTraits + cls.pyre_inheritedTraits
    for trait in traits:
        if isElementFacility(trait):
            return True
        continue
    return False


def isElementFacility(trait):
    from ..descriptors import ElementInterface
    import pyre
    return isinstance(trait, pyre.facility) and trait.type is ElementInterface


# version
__id__ = "$Id$"

# End of file 
