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
    key = cls.elementtype, cls.name
    if key in all_action_classes:
        registered = all_action_classes[key]
        if registered is cls:
            return
        m = "{.__name__!r} is in conflict with {.__name__!r}".format(
            cls, registered)
        raise RuntimeError(m)
    
    all_action_classes[key] = cls
    return cls


def registerAllActions(package):
    """register all actions in the given package"""
    return package.registerAllActions()



# implementations

# list of all action classes
all_action_classes = {}


# End of file 
