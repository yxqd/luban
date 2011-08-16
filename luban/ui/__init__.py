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


class ElementClassProxy:


    def __getattr__(self, name):
        from .elements._registry import fundamental_elements
        e = fundamental_elements.getElementClass(name)
        if e is None:
            raise AttributeError(name)
        return e


e = ElementClassProxy()
del ElementClassProxy


from . import elements, actions

registerElementProvider = elements.registerElementProvider


# version
__id__ = "$Id$"

# End of file 
