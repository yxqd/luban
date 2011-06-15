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


from .Action import Action as base

class SimpleAction(base):


    actionname = descriptors.str()
    params = descriptors.dict()


    def identify(self, inspector):
        return inspector.onSimpleAction(self)


    def __init__(self, actionname, **params):
        super(SimpleAction, self).__init__(actionname=actionname, params=params)
        return



# version
__id__ = "$Id$"

# End of file 

