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


from .meta import Meta
from .AbstractAttributeContainer import AbstractAttributeContainer
class AttributeContainer(AbstractAttributeContainer, metaclass=Meta):


    @classmethod
    def __get_subclass_preparation_context__(cls):
        from . import descriptors, validators
        return {
            'descriptors': descriptors,
            'd': descriptors,
            'validators': validators,
            'v': validators,
            }
    

    @classmethod
    def iterDescriptors(cls):
        from .meta.DescriptorCollector import STORE_NAME
        return getattr(cls, STORE_NAME).values()
    
    
    @classmethod
    def getDescriptor(cls, name):
        return getattr(cls, name)    
    
    
    def setAttribute(self, name, value):
        trait = self.getDescriptor(name)
        trait.__set__(self, value)
        return value


    def getAttribute(self, name):
        trait = self.getDescriptor(name)
        return trait.__get__(self, self.__class__)


    def iterAttributes(self):
        for descriptor in self.iterDescriptors():
            name = descriptor.name
            value = descriptor.__get__(self, self.__class__)
            yield name, value
            continue
        return

    pass


# version
__id__ = "$Id$"

# End of file 
