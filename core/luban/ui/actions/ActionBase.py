#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao  Lin
#                      California Institute of Technology
#                      (C) 2005-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from .AttributeContainer import AttributeContainer, Meta
class ActionBase(AttributeContainer):

    """base class of all actions
    """

    # decorations
    abstract = True

    # don't override this
    lubanaction = descriptors.bool(default=True)

    
    @classmethod
    def getCtorDocStr(
        cls,
        ctor_name=None,
        ):
        names = 'lubanaction', 'element'
        
        from luban.ui.descriptors.EventHandler import EventHandler
        skip = lambda descriptor: isinstance(descriptor, EventHandler) \
               or descriptor.name in names
        
        from ..AttributeContainer import generateCtorDocStr        
        return generateCtorDocStr(cls, ctor_name=ctor_name, skip=skip)
    

# End of file 
