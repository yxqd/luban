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


"""
this could be used to describe simple element actions
in a more arbitrary way, when combined with ArbitraryElementActionFactory.
This class is not in use at this moment.
"""


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from .ElementActionBase import ElementActionBase as base
class SimpleElementAction(base):

    # decorations
    

    # attributes
    actionname = descriptors.str() # name of the action
    params = descriptors.dict() # parameters of the action
    
    
    # overload ctor to provide better interface
    def __init__(self, element=None, actionname=None, **params):
        super().__init__(element=element, actionname=actionname, params=params)
        return


    def identify(self, inspector):
        return inspector.onSimpleElementAction(self)


# version
__id__ = "$Id$"

# End of file 

