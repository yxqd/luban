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


#  for controller access
def load(*args, **kwds):
    from .Loading import Loading
    return Loading(*args, **kwds)


# version
__id__ = "$Id$"

# End of file 
