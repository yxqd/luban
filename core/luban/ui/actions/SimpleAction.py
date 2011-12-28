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


# is this really in use?


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from .Action import Action as base

class SimpleAction(base):

    """simple actions that can be described by its name and its parameters
    """

    # decorations

    
    # attributes
    actionname = descriptors.str()
    params = descriptors.dict()

    
    # methods
    def identify(self, inspector):
        return inspector.onSimpleAction(self)


    # overload ctor to provide better interface
    def __init__(self, actionname, **params):
        super().__init__(actionname=actionname, params=params)
        return



# version
__id__ = "$Id$"

# End of file 

