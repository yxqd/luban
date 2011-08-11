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
descriptors for luban type system
"""


from .. import schema


# descriptors of simple types
def str(default="", dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.str
    p.default = default
    return p

def int(default=0, dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.int
    p.default = default
    return p

def bool(default=False, dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.bool
    p.default = default
    return p

def date(default=None, dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.date
    p.default = default
    return p


# descriptors of complex types
def list(default=None, dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.list
    p.default = default if default is not None else ()
    return p

def dict(default=None, dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.dict
    p.default = default if default is not None else {}
    return p

def ordered_dict(default=None, dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.ordered_dict
    import collections
    p.default = default if default is not None else collections.OrderedDict()
    return p



# descriptors for ui elements and actions
def action(default=None):
    p = Property()
    p.type = schema.action
    if default is None:
        from ..actions.NoAction import NoAction
        default = NoAction()
    p.default = default
    return p

def element(default=None, dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.element
    if default is None:
        from ..elements.NoElement import NoElement
        default = NoElement()
    p.default = default
    return p

def object(default=None, dynamic=True):
    p = _prop(dynamic=dynamic)
    p.type = schema.object
    p.default = default
    return p



# misc descriptors
def guid():
    from .GUID import GUID
    d = GUID()
    d.type = schema.str
    d.default = ""
    return d



# implementation details
from .Property import Property
from .DynamicProperty import DynamicProperty
def _prop(dynamic):
    if dynamic:
        return DynamicProperty()
    return Property()


import luban._journal as journal
debug = journal.debug('luban.content.descriptors')


# version
__id__ = "$Id$"

# End of file 
