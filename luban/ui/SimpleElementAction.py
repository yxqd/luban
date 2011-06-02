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


from ElementActions import ElementActions
from Action import Action as base

class SimpleElementAction(ElementActions, base):


    abstract = False


    element = base.descriptors.reference(name='element')
    actionname = base.descriptors.str(name='actionname')
    params = base.descriptors.dict(name='params')
    
    def __init__(self, element, actionname, **params):
        super(SimpleElementAction, self).__init__(element=element, actionname=actionname, params=params)
        return


    def identify(self, inspector):
        return inspector.onSimpleElementAction(self)


# version
__id__ = "$Id$"

# End of file 

