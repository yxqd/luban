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


from pyre.components.properties import *
import pyre

class ActionInterface(pyre.interface, family="luban.ui.actions"):

    """
    Interface declarator for actions
    """


class ElementInterface(pyre.interface, family="luban.ui.elements"):

    """
    Interface declarator for elements
    """


def action():
    from .actions.NoAction import NoAction
    return facility(interface=ActionInterface, default=NoAction)


def element(default=None):
    return facility(interface=ElementInterface, default=default)


def object(default=None):
    if default is None:
        from .AttributeContainer import AttributeContainer as default
    return pyre.components.properties.object(default=default)


def list(default=None):
    d = Property()
    from ._schema import List
    d.type = List
    d.default = default if default is not None else ()
    return d


def dict(default=None):
    d = Property()
    from ._schema import Dict
    d.type = Dict
    d.default = default if default is not None else {}
    return d


def ordered_dict(default=None):
    d = Property()
    from ._schema import OrderedDict
    d.type = OrderedDict
    import collections
    d.default = default if default is not None else collections.OrderedDict()
    return d


def guid():
    d = GUID()
    from pyre.schema import str
    d.type = str
    d.default = ""
    return d


def lists(**kwds):
    return Lists(**kwds)


def date(**kwds):
    return Date(**kwds)


#???
def link(**kwds):
    return Link(**kwds)



DescriptorBase = Property

class GUID(Property):


    def __get__(self, instance, cls):
        id = super().__get__(instance, cls)
        if not id:
            from .GUID import GUID as getguid
            id = getguid(instance)
            instance.id = id
        return id


    def __set__(self, instance, value):
        if value:
            value = self._check(value)
        return super().__set__(instance, value)


    def _check(self, value):
        value = __builtins__['str'](value)

        # verify
        if value.find('.') != -1:
            raise ValueError("id cannot contain '.': %s" % value)
        
        return value


class Lists(Property):

    # list of lists

    def __init__(self, name=None, default=None, meta=None, validator=None):
        default = self._cast(default)
        Property.__init__(self, name, "lists", default, meta, validator)
        return


    def _cast(self, value):
        list = __builtins__['list']
        if not value: return [[]]
        try:
            ret = []
            for item in value:
                ret.append(list(item))
                continue

        except:
            raise RuntimeError('cannot cast %s' % (value,))

        return ret



class Date(Property):

    # dictionary

    def __init__(self, name=None, default=None, meta=None, validator=None, format=None):
        if not format:
            format = '%b %d, %Y'
        self.format = format
        default = self._cast(default)
        Property.__init__(self, name, "date", default, meta, validator)
        return


    def _cast(self, value):
        # default
        import datetime
        if not value: return datetime.date.today()
        
        # cast from string
        if isinstance(value, str):
            import time
            t = time.strptime(value, self.format)
            return datatime.date(t[:3])
        
        # tuple of year, month, day
        if isinstance(value, tuple) and len(value)==3:
            return datatime.date(t)
        
        raise NotImplementedError


    def tostr(self, value):
        return value.strftime(self.format)



# ???
# describe a link
class  Link(Property):

    # dictionary

    def __init__(self, name=None, default=None, meta=None, validator=None):
        default = self._cast(default)
        Property.__init__(self, name, "link", default, meta, validator)
        return


    def _cast(self, value):
        from luban.content.Link import Link
        return value or Link()


import luban._journal as journal
debug = journal.debug('luban.content.descriptors')


# version
__id__ = "$Id$"

# End of file 
