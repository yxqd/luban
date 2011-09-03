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

__all__ = [
    'str', 'int', 'bool', 'date',
    'list', 'dict', 'ordered_dict',
    'action', 'element', 'object',
    ]


from .. import schema


# descriptors of simple types
def str(default=None, dynamic=True):
    p = _prop(schema.str, dynamic=dynamic)
    p.default = default
    return p

def int(default=0, dynamic=True):
    p = _prop(schema.int, dynamic=dynamic)
    p.default = default
    return p

def bool(default=False, dynamic=True):
    p = _prop(schema.bool, dynamic=dynamic)
    p.default = default
    return p

def date(default=None, dynamic=True):
    p = _prop(schema.date, dynamic=dynamic)
    p.default = default
    return p


# descriptors of complex types
def list(default=None, dynamic=True):
    p = _prop(schema.list, dynamic=dynamic)
    p.default = default
    return p

def dict(default=None, dynamic=True):
    p = _prop(schema.dict, dynamic=dynamic)
    p.default = default
    return p

def ordered_dict(default=None, dynamic=True):
    p = _prop(schema.ordered_dict, dynamic=dynamic)
    p.default = default
    return p



# descriptors for ui elements and actions
def action(default=None):
    p = _prop(schema.action, dynamic=False)
    if default is None:
        from ..actions.NoAction import NoAction
        default = NoAction()
    p.default = default
    return p


# eventhandler is an action to be performed when an event happens
def eventhandler(default=None, eventtype=None):
    if default is None:
        from ..actions.NoAction import NoAction
        default = NoAction()
    from .EventHandler import EventHandler
    h = EventHandler()
    h.default = default
    h.eventtype = eventtype
    return h


def element(default=None, dynamic=True):
    p = _prop(schema.element, dynamic=dynamic)
    if default is None:
        from ..elements.NoElement import NoElement
        default = NoElement()
    p.default = default
    return p

def object(default=None, dynamic=True):
    p = _prop(schema.object, dynamic=dynamic)
    p.default = default
    return p


# misc descriptors
def id():
    from .ID import ID
    return ID()


# implementation details
from .Property import Property
from .DynamicProperty import DynamicProperty
def _prop(type, dynamic):
    typename = type.__name__
    if dynamic:
        base = DynamicProperty
        descriptor_type_name = "Dynamic" + typename
        docstr = "Dynamic %s descriptor: value can either be of %s type or an action that evaluates to %s type" % (typename, typename, typename)
    else:
        base = Property
        descriptor_type_name = typename
        docstr = "%s descriptor" % typename
    
    from . import _generated_descriptor_types as store
    template = "%s%s descriptor"
    if not hasattr(store, descriptor_type_name):
        class K(base): 
            __doc__ = docstr
            pass
        K.__name__ = descriptor_type_name
        K.type = type
        setattr(store, descriptor_type_name, K)
    K = getattr(store, descriptor_type_name)
    return K()


from luban import journal
debug = journal.debug('luban.content.descriptors')


# version
__id__ = "$Id$"

# End of file 
