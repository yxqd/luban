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


from .ActionBase import ActionBase
from ..meta.TypeRegistryCurator import registry


# public interface
action_types = None


# implementations
# proxy that looks like a registry of action types
class ActionTypes:


    def __init__(self):
        self.registry = registry
        self.names = [] # a list of type names
        return


    def getActionClass(self, name):
        k = self.registry.get(name)
        if k is None:
            return
        if not issubclass(k, ActionBase):
            return
        return k


    def onRegistration(self, cls):
        if issubclass(cls, ActionBase):
            self.names.append(cls.__unique_type_name__)
        return
    

action_types = ActionTypes()
registry.observers.append(action_types)


# End of file 
