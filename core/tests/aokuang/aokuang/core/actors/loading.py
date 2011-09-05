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
button
"""

import luban.ui as lui

from ...ObjectActor import Actor as base
class Actor(base):

    expose = True
    
    def __init__(self):
        title = "action 'loading'"
        interface_factory = InterfaceFactory()
        interface_factory.actor = self.name
        super().__init__(title=title, interface_factory = interface_factory)
        return
    
    pass # Actor


from ...ObjectInterface import Factory as base
class InterfaceFactory(base):

    from luban.ui.actions.Loading import Loading as object_type
    
    pass # InterfaceFactory


__all__ = ['Actor']

# End of file 

