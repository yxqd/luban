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


from .ElementActionFactory import ElementActionFactory
from .SelectingActionBase import SelectingActionBase as base, Meta
class SelectByIDandType(ElementActionFactory, base, metaclass=Meta):

    # decorations
    simple_description = 'select an element by its ID and optionally its type'
    full_description = (
        "This action selects an element using its ID and optionally its type. "
        "The constructed selector can be used to perform further "
        "actions on the selected element. Eg. selector.destory(). "
        )
    abstract = False

    # attributes
    id = descriptors.str()
    type = descriptors.str()

    # for inspector
    def identify(self, inspector):
        return inspector.onSelectByIDandType(self)
    

# version
__id__ = "$Id$"

# End of file 

