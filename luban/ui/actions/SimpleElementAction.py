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


"""
this could be used to describe simple element actions
in a more arbitrary way, when combined with ArbitraryElementActionFactory.
This class is not in use at this moment.
"""


from .ElementActionBase import ElementActionBase as base
class SimpleElementAction(base):


    abstract = False


    # attributes
    actionname = descriptors.str() # name of the action
    params = descriptors.dict() # parameters of the action
    
    
    def __init__(self, element=None, actionname=None, **params):
        super().__init__(element=element, actionname=actionname, params=params)
        return


    def identify(self, inspector):
        return inspector.onSimpleElementAction(self)


# version
__id__ = "$Id$"

# End of file 

