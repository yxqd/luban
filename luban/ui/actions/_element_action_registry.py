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
    all_action_classes.append(cls)
    return cls


def registerAllActions(package):
    """register all actions in the given package"""
    return package.registerAllActions()



# implementations

# list of all action classes
all_action_classes = []


# End of file 
