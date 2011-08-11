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
    def __prepare__(cls, name, bases, **kwds):
        d = super().__prepare__(name, bases, **kwds)
        context = cls._collectContextFromBases(bases)
        d.update(context)
        return d

    
    @classmethod
    def _collectContextFromBases(cls, bases):
        """collect context for preparation of the target class of this meta class
        from bases of the target class.
        """
        context = dict()
        
        # only check the farthest one in the immediate parent classes
        base = bases[-1]
        
        method = "__get_subclass_preparation_context__"
        # first check that parent class itself
        if hasattr(base, method):
            c = getattr(base, method)()
            context.update(c)
        else:
            # if not found, check all bases of that parent class
            for base1 in base.__mro__:
                if hasattr(base1, method):
                    c = getattr(base1, method)()
                    context.update(c)
                    break # assume all implementation of __get_subclass_preparation_context__ to call super correctly
                continue
                
        return context



from .AbstractAttributeContainer import AbstractAttributeContainer
class AttributeContainer(pyre.component, AbstractAttributeContainer, metaclass=Meta):

    from .descriptors import DescriptorBase

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
