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


from .ElementActions import ElementActions
from .Action import Action as base

class SelectByID(ElementActions, base):

    simple_description = 'select an element by its ID'
    full_description = (
        "This action selects an element using its ID. "
        "The constructed selector can be used to perform further "
        "actions on the selected element. Eg. selector.destory(). "
        "Please refer to each individual element types for those "
        "actions. "
        )

    abstract = False

    id = base.descriptors.str(name='id')


    def identify(self, inspector):
        return inspector.onSelectByID(self)
    

# version
__id__ = "$Id$"

# End of file 

