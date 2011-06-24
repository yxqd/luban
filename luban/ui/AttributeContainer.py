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


# metaclass
from pyre.components.Actor import Actor as _metabase
class Meta(_metabase):

    @classmethod
    def __prepare__(cls, name, bases, predefined=None, **kwds):
        from luban.ui.OrderedDictWithPredefinedSymbols import OrderedDictWithPredefinedSymbols
        d = OrderedDictWithPredefinedSymbols()

        if predefined is None:
            from .PredefinedSymbols import PredefinedSymbols
            predefined = PredefinedSymbols()
            
        d.predefined = predefined
        return d



from .AbstractAttributeContainer import AbstractAttributeContainer
class AttributeContainer(pyre.component, AbstractAttributeContainer, metaclass=Meta):

    from .descriptors import DescriptorBase

    @classmethod
    def iterDescriptors(cls):
        return cls.pyre_getTraitDescriptors()

    
    @classmethod
    def getDescriptor(cls, name):
        return cls.pyre_getTraitDescriptor(name)
    
    
    
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
