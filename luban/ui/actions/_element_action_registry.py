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
    actionclassname = cls.__name__
    key = element_type, factory

    # init container if necessary
    if element_type not in element2actionclassnames:
        element2actionclassnames[element_type] = []
    
    if not luban.extension_allow_override:
        # if class name already used, we have a problem
        if actionclassname in element2actionclassnames[element_type]:
            m = "failed to regsiter {0.__name__!r}: action factory name {1!r} already used.".format(cls, factory)
            raise ConflictAction(m)
        
        # if the key already exists, we have a problem
        if key in all_action_classes:
            registered = all_action_classes[key]
            m = "{.__name__!r} is in conflict with {.__name__!r}".format(
                cls, registered)
            raise ConflictAction(m)
    
    all_action_classes[key] = cls
    element2actionclassnames[element_type].append(actionclassname)
    
    return cls


def registerAllActions(package):
    """register all actions in the given package"""
    return package.registerAllActions()


# implementations

# (element_type, action factory method name) -> action class 
all_action_classes = {}

# element_type -> list of action class names
element2actionclassnames = {}

# misc
from .exceptions import ConflictAction

# End of file 
