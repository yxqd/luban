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


def action():
    return facility(interface=ActionInterface)


def lists(**kwds):
    return Lists(**kwds)

def dict(**kwds):
    return Dict(**kwds)

def date(**kwds):
    return Date(**kwds)


#???
def link(**kwds):
    return Link(**kwds)


def str(*args, **kwds):
    return String(*args, **kwds)
_builtin_str = __builtins__['str']




DescriptorBase = Property



class EventHandler(Facility):
    
    pass


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


class Dict(Property):

    # dictionary

    def __init__(self, name=None, default=None, meta=None, validator=None):
        default = self._cast(default)
        Property.__init__(self, name, "dict", default, meta, validator)
        return


    def _cast(self, value):
        # 
        return value or {}



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


class String(Property):

    def _cast(self, v):
        try:
            return _builtin_str(v)
        except:
            # import traceback
            # debug.log(traceback.format_exc())
            return str(v)


import luban._journal as journal
debug = journal.debug('luban.content.descriptors')


# version
__id__ = "$Id$"

# End of file 
