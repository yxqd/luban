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


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# assumption: any descriptor of element type
# is regarded as describing a subelement
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


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
        self._register(name, cls)
        return


    def getElementClass(self, name):
        return self._store.get(name)


    def _register(self, name, cls):
        # already registered, skip
        if cls in self._store.values():
            return
        
        import luban
        if not luban.extension_allow_override:
            if name in self._store:
                # conflict
                m = "element type of the same name already registered. name: %s, new element: %s, existing element: %s" % (name, cls, self._store[name])
                from .exceptions import ConflictElement
                raise ConflictElement(m)

        # register
        self._store[name] = self._store[name.lower()] = cls
        self._cls2name[cls] = name
        return


    def _getUniqueName(self, target):
        # get unique name to identify the element type
        sig  = '__unique_type_name__'
        if sig in target.__dict__:
            name = target.__dict__[sig]
        else:
            name = target.__name__
            # set it to the class
            setattr(target, sig, name)
        return name


fundamental_elements = FundamentalElements()


#
def hasSubElements(cls):
    traits = cls.iterDescriptors()
    for trait in traits:
        if isSubElementDescriptor(trait):
            return True
        continue
    return False


def isSubElementDescriptor(trait):
    from ..schema import element
    return trait.type is element


# version
__id__ = "$Id$"

# End of file 
