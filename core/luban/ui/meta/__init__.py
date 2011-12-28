# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
meta classes
"""

from luban import py_major_ver

from .SubclassDefinitionContextBuilder import SubclassDefinitionContextBuilder
from .DescriptorCollector import DescriptorCollector
from .TypeRegistryCurator import TypeRegistryCurator

if py_major_ver == 2:
    class Meta(DescriptorCollector):
        def __new__(cls, name, bases, attributes, **kwds):
            created = DescriptorCollector.__new__(cls, name, bases, attributes, **kwds)
            from .TypeRegistry import registry
            registry.register(created)
            return created
        
    
elif py_major_ver == 3:
    class Meta(SubclassDefinitionContextBuilder, TypeRegistryCurator, DescriptorCollector): pass


# End of file 
