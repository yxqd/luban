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


import luban

from ....ElementInterface import Factory as base
class InterfaceFactory(base):

    from luban.ui.elements.Element import Element as object_type
    panel_title = "luban ui element base class"
    full_description = (
        "This base class itself cannot be instantiated to meaningful ui elements. " 
        "Instead, here we show the common API of all "
        "normal luban ui elements."
        )

    pass # InterfaceFactory


from ....ObjectActor import Actor as base
class Actor(base):

    expose = True
    frame_title = "luban ui element base class"
    interface_factory = InterfaceFactory()
    py_pkg_name = __name__
    py_pkg_path = __file__

    pass # Actor


__all__ = ['Actor']

# End of file 

