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
methods here create instances of action classes

Each action class describe one type of action.
Keep in mind that in luban.ui.actions we are using data objects to 
hold information about actions, instead of actually
performing actions.
The desriptions here will later be translated by renderers
to actual actions in different media.
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
    ]
def importAllElementActions():
    modules = action_modules
    for name in modules:
        __import__(name, fromlist=['.'], globals=globals())
        continue
    return
importAllElementActions()
del importAllElementActions


# version
__id__ = "$Id$"

# End of file 
