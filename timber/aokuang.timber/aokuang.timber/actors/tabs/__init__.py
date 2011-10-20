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

    from luban.ui.elements.Tabs import Tabs as object_type
    
    pass # InterfaceFactory


from ....ObjectActor import Actor as base
class Actor(base):

    expose = True
    frame_title = "luban element: tabs"
    interface_factory = InterfaceFactory()

    py_pkg_name = __name__
    py_pkg_path = __file__
    def _findDemoPanels(self):
        panels = super()._findDemoPanels()

        from aokuang.core.actors import tabs
        self.py_pkg_name = tabs.__name__
        self.py_pkg_path = tabs.__file__
        panels += super()._findDemoPanels()
        return panels
    
    pass # Actor


__all__ = ['Actor']

# End of file 

