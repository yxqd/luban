#!/usr/bin/env python
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


from .Element import Element


class ReSTDocument(Element):

    abstract = False

    def identify(self, inspector):
        return inspector.onReSTDocument(self)

    text = descriptors.list()

    def __init__(self, *args, **kwds):
        import warnings
        warnings.warn("ReSTDocument is obsolete, please use ReStructuredTextDocument)", DeprecationWarning)
        Element.__init__(self, *args, **kwds)


# version
__id__ = "$Id$"

# End of file