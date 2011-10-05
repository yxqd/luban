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


from luban.ui.actions.Loading import Loading as base

class SetAnchor(base):

    # decorations
    simple_description = 'anchor of a UI'
    full_description = (
        )

    # attributes
    
    def identify(self, inspector):
        return inspector.onSetAnchor(self)


# version
__id__ = "$Id$"

# End of file 

