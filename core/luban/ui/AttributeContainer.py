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


from luban import py_major_ver

AttributeContainerBase = Meta(
    'AttributeContainerBase', (AbstractAttributeContainer,), {}
    )


class AttributeContainer(AttributeContainerBase):
    
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
    def iterDescriptorNames(cls):
        from .meta.DescriptorCollector import STORE_NAME
        return getattr(cls, STORE_NAME).keys()
    
    
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
    
    
    # default ctor implementation
    def __init__(self, attributes=None, **kwds):
        """AttributeContainer(<attributes>, **attributes)

        Eg:
        AttributeContainer(key1=val1, key2=val2, ...)
        AttributeContainer({key1:val1, key2:val2})
        AttributeContainer({key1:val1, key2:val2}, key3=val3)
        
        attributes has higher priority over kwds
        """
        # AbstractAttributeContainer is abstract, we really don't
        # need its ctor to have any effects
        # super().__init__() 

        attributes = attributes or {}
        kwds.update(attributes)
        
        for k, v in kwds.items():
            debug.log('setting attribute %r to %s' % (k,v))
            self.setAttribute(k,v)
            continue

        return
    
    
    # helper methods
    @classmethod
    def getCtorDocStr(
        cls,
        ctor_name=None,
        skip = None
        ):
        """produce a docstr for the ctor

        This method loop over all descriptors and create
        the ctor docstr by extracting metadata from the descriptors
        
        ctor_name: name of the constructor. could be name of a factory method too
        skip: skip(descriptor) -> True means to skip a descriptor
        """
        return generateCtorDocStr(cls, ctor_name=ctor_name, skip=skip)
    

    def __repr__(self):
        t = self.__class__.__name__
        ps = list(self.iterAttributes())
        ps = ', '.join('%s=%s' % (k,v) for k,v in ps)
        return t + '(' + ps + ')'

    pass



from luban import journal
debug = journal.debug('luban.ui.AttributeContainer')




def generateCtorDocStr(
    cls,
    ctor_name=None,
    skip = None
    ):
    """produce a docstr for the ctor

    This method loop over all descriptors and create
    the ctor docstr by extracting metadata from the descriptors

    ctor_name: name of the constructor. could be name of a factory method too
    skip: skip(descriptor) -> True means to skip a descriptor
    """
    descriptors = cls.iterDescriptors()
    l = []
    for descriptor in descriptors:
        # skip ?
        if skip and skip(descriptor): continue

        # anything startswith "luban" is "system-related".
        # don't make it public
        name = descriptor.name
        if name.startswith('luban'):
            continue

        value = descriptor.default

        l.append('%s=%r' % (name, value))
        continue
    ctor_name = ctor_name or cls.__name__

    indent = '  '
    s = [ctor_name + '(']
    for i in range(0, len(l), 3):
        t = indent + ', '.join(l[i: i+3]) + ','
        s.append(t)
        continue
    s.append(indent + ')')
    return '\n'.join(s)
    

# End of file 
