# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from ..decorators import *


def allowedWidgets(widgets):
    def _(method):
        method.allowed_widgets = widgets
        return method
    return _


def elementfactory(method):
    """decorate a method to be an element factory method
    """
    if not method.__doc__:
        raise NotImplementedError("should add docstr to %s" % method)
    method.iselementfactory = True
    return method


def subelementfactory(subelem, container):
    """create a decorator that transforms a method to a subelement factory method
    of the container class
    """
    def decorate(method):
        factory = method.__name__
        method.__doc__ = subelem.getCtorDocStr(ctor_name = factory)
        decorated = elementfactory(method)
        setattr(container, factory, decorated)
        return decorated
    return decorate


# version
__id__ = "$Id$"

# End of file 
