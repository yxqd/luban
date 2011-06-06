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


class CodeViewer(Element):

    abstract = False
    experimental = True

    def identify(self, inspector):
        return inspector.onCodeViewer(self)

    syntax = descriptors.str(name='syntax')
    text = descriptors.str(name='text')


# version
__id__ = "$Id$"

# End of file
