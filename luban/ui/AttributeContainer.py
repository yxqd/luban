# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# use pyre inventory to implement attributecontainer.
# we can reimplement this later


from pyre.inventory.Inventory import Inventory
class AttributeContainer( Inventory):

    import descriptors

    def getDescriptors(cls):
        # return a list of descriptors
        return cls._traitRegistry.values()
    getDescriptors = classmethod(getDescriptors)


    def setAttribute(self, name, value):
        trait = self.getTrait(name)
        trait._set(self, value, locator)
        return


    def iterAttributeKeyValPairs(self):
        for descriptor in self.getDescriptors():
            name = descriptor.name
            value = descriptor.__get__(self)
            yield name, value


    def __init__(self, name=None):
        name = name or (self.__class__.__name__ + str(id(self)) )
        Inventory.__init__(self, name)
        return

    
    def getCtorDocStr(cls, descriptors=None):
        if not descriptors:
            descriptors = cls.getDescriptors()
        l = []
        for descriptor in descriptors:
            name = descriptor.name
            value = descriptor.default
            l.append('%s=%r' % (name, value))
            continue
        return '%s(%s)' % (cls.__name__, ', '.join(l))
    getCtorDocStr = classmethod(getCtorDocStr)


    # XXX: this does not work for self referencing entities.
    # XXX: need to think about this sometime
    # def __str__(self):
    #    props = ['%s=%s' % (k,v) for k,v in self.iterAttributeKeyValPairs()]
    #    props = ', '.join(props)
    #    return '%s(%s)' % (self.__class__.__name__, props)

    pass


import pyre.parsing.locators
locator = pyre.parsing.locators.simple('luban.AttributeContainer')


# version
__id__ = "$Id$"

# End of file 
