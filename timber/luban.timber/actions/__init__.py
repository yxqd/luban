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
At this moment only a few actions are ported to 0.4. 
see "action_modules" below.

TODO: 
* credential related actions
* element actions in the modules in this subpackage
"""


#  for credentials
def createCredential(**kwds):
    '''createCredential(username=..., ticket=...)
    '''
    from .SimpleAction import SimpleAction
    return SimpleAction('credentialCreation', **kwds)


def updateCredential(**kwds):
    '''updateCredential(username=..., ticket=...)
    '''
    from .SimpleAction import SimpleAction
    return SimpleAction('credentialUpdate', **kwds)


def removeCredential():
    from .SimpleAction import SimpleAction
    return SimpleAction('credentialRemoval')


# common element actions
action_modules = [
    'element_common_actions',
    'SetAnchor',
    ]
def importAllActions():
    modules = action_modules
    for name in modules:
        __import__(name, fromlist=['.'], globals=globals())
        continue
    return
importAllActions()
del importAllActions


# version
__id__ = "$Id$"

# End of file 
