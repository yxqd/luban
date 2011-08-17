# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# public interface
action_types = None


# implementations
# proxy that looks like a registry of action types
class ActionTypes:


    def __init__(self):
        from ..meta.TypeRegistryCurator import registry
        self.registry = registry
        return


    def getActionClass(self, name):
        k = self.registry.get(name)
        if k is None:
            return
        from .ActionBase import ActionBase
        if not issubclass(k, ActionBase):
            return
        return k


action_types = ActionTypes()


# version
__id__ = "$Id$"

# End of file 
