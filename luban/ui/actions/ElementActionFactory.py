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


from .CommonElementActionFactory import CommonElementActionFactory


#class ElementActionFactory(CommonElementActionFactory):

class ElementActionFactory:

    """factory of element actions
    """

    def __getattr__(self, name):
        from ._element_action_registry import all_action_classes
        key = self.type, name
        if key not in all_action_classes:
            raise AttributeError(name)
        
        cls = all_action_classes[key]
        def _(**kwds):
            return cls(element=self, **kwds)
        _.__name__ = name
        return _
    
    pass


# version
__id__ = "$Id$"

# End of file 

