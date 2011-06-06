# -*- Python -*-
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


import pyre

from .AbstractAttributeContainer import AbstractAttributeContainer
class AttributeContainer(pyre.component, AbstractAttributeContainer):

    from . import descriptors
    from .descriptors import DescriptorBase

    @classmethod
    def getDescriptors(cls):
        # return a list of descriptors
        return [item for item in cls.__dict__.values()
                if isinstance(item, cls.DescriptorBase)]


    
    @classmethod
    def getDescriptor(cls, name):
        return getattr(cls, name)
    
    
    
    def setAttribute(self, name, value):
        trait = self.getDescriptor(name)
        trait.__set__(self, value)
        return


    def getAttribute(self, name):
        trait = self.getDescriptor(name)
        return trait.__get__(self)


    def iterAttributes(self):
        for descriptor in self.getDescriptors():
            name = descriptor.name
            value = descriptor.__get__(self)
            yield name, value


    pass


# version
__id__ = "$Id$"

# End of file 
