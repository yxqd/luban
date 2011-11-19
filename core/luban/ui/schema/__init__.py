# -*- python -*-
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
This subpackage contains types supported by luban

Luban only support a very limited set of types intentionally.
These are types that are useful for user interface.

"""

# primitive types
from .Boolean import Boolean as bool
from .Integer import Integer as int
from .String import String as str
from .Date import Date as date
primitive_types = [bool, int, str, date]

# container types
from .List import List as list
from .Dict import Dict as dict
from .OrderedDict import OrderedDict as ordered_dict
container_types = [list, dict, ordered_dict]

# luban ui "component" types
from .Object import Object as object
from .Element import Element as element
from .Action import Action as action
component_types = [object, element, action]

all_types = primitive_types + container_types + component_types


def valid_luban_value(v):
    for t in all_types:
        try:
            t.__cast__(v)
        except:
            pass
        else:
            return False
    return True


# Implementation:
# the implementation here were derived from pyre 1.0 pyre.schema


# version
__id__ = "$Id$"

# End of file 
