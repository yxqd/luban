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

"""
AttributeContainer: base class of luban objects

TOTHINK:
* do we want to implement slots like behavior?

"""

from .meta import Meta
from .AbstractAttributeContainer import AbstractAttributeContainer
class AttributeContainer(AbstractAttributeContainer, metaclass=Meta):

    """base class of all luban types
    """

    # exceptions
    from .meta.exceptions import TypeConflict
    

    # subclasses of AttributeContainer are either
    # luban types, or base classes for them
    # to tell the differences of them, here we define
    # attribute "abstract" to
    # indicate whether a class is a base class (abstract is True)
    # or a real luban type (abstract is False)
    abstract = True
    

    @classmethod
    def __get_subclass_preparation_context__(cls):
        from . import descriptors, validators
        return {
            'descriptors': descriptors,
            'validators': validators,
            
            # XXX: is it really a good idea to have aliases?
            'd': descriptors,
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

    
    def __repr__(self):
        t = self.__class__.__name__
        ps = list(self.iterAttributes())
        ps = ', '.join('%s=%s' % (k,v) for k,v in ps)
        return t + '(' + ps + ')'

    pass


# version
__id__ = "$Id$"

# End of file 