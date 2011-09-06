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


import luban.ui as lui

from ....ObjectInterface import Factory as base
class InterfaceFactory(base):

    from luban.ui.actions.Loading import Loading as object_type
    skip_descriptors = ['lubanaction']
    
    pass # InterfaceFactory


from ....ObjectActor import Actor as base
class Actor(base):

    expose = True
    frame_title = "luban action: loading"
    interface_factory = InterfaceFactory()
    py_pkg_name = __name__
    py_pkg_path = __file__
    
    pass # Actor


__all__ = ['Actor']

# End of file 

