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


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from .ElementActionFactory import ElementActionFactory
from .SelectingActionBase import SelectingActionBase as base, Meta
_selectbyidandtype = Meta(
    '_selectbyidandtype',
    (ElementActionFactory, base),
    {'abstract': 1}
    )
class SelectByIDandType(_selectbyidandtype):

    # decorations
    simple_description = 'select an element by its ID and optionally its type'
    full_description = (
        "This action selects an element using its ID and optionally its type. "
        "The constructed selector can be used to perform further "
        "actions on the selected element. Eg. selector.destory(). "
        )

    # attributes
    id = descriptors.str()
    type = descriptors.str()

    # for inspector
    def identify(self, inspector):
        return inspector.onSelectByIDandType(self)
    

# version
__id__ = "$Id$"

# End of file 

