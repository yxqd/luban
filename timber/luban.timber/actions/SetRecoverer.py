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

class SetRecoverer(base):

    # decorations
    simple_description = 'the parameters here can be used to reconstruct the state of the UI app using a loading action'
    full_description = (
        )

    # attributes
    
    def identify(self, inspector):
        return inspector.onSetRecoverer(self)


# version
__id__ = "$Id$"

# End of file 

