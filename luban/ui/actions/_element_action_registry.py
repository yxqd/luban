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


"""registry of element action types

purpose of this registry:

* make sure we can recover an action type from (selected element type, action factory name)
* detect conflicts 
  two actions cannot have the same element type and the action factory name
"""



# public interface
def register(cls):
    import luban

    # if already registered, do nothing
    if cls in all_action_classes.values():
        return

    # key of an action type
    element_type = cls.element_type
    if element_type is not None:
        element_type = element_type.__unique_type_name__
    factory = cls.factory_method
    key = element_type, factory

    if not luban.extension_allow_override:
        # if the key already exists, we have a problem
        if key in all_action_classes:
            registered = all_action_classes[key]
            m = "{.__name__!r} is in conflict with {.__name__!r}".format(
                cls, registered)
            raise ActionFactoryMethodConflict(m)
    
    all_action_classes[key] = cls
    
    return cls


def registerAllActions(package):
    """register all actions in the given package"""
    return package.registerAllActions()


all_action_classes = None


# implementations

# (element_type, action factory method name) -> action class 
all_action_classes = {}

# misc
from .exceptions import ActionFactoryMethodConflict

# End of file 
