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


from luban.ui.elements.SimpleElement import SimpleElement as base
class CodeViewer(base):

    experimental = True

    # decorations
    simple_description = 'code viewer'
    full_description = (
        ''
        )

    # properties
    syntax = descriptors.str()
    text = descriptors.str()
    
    # methods
    def identify(self, inspector):
        return inspector.onCodeViewer(self)



# version
__id__ = "$Id$"

# End of file
