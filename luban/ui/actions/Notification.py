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


from .Action import Action as base

class Notification(base):


    abstract = False


    element = descriptors.reference()
    event = descriptors.str()
    actor = descriptors.str()
    routine = descriptors.str()
    params = descriptors.dict()
    
    
    def __init__(self, element, event, actor, routine=None, **params):
        super(Notification, self).__init__('notification')
        self.element = self.elementSelector(element)
        self.event = event
        self.actor = actor
        self.routine = routine
        self.params = params
        return
    
    
    def identify(self, inspector):
        return inspector.onNotification(self)
    
    
# version
__id__ = "$Id$"

# End of file 

