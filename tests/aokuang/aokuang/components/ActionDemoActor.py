# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import luban.content as lc

from UIElementDemoActor import Actor as base, panel, example, quickpanel

class Actor(base):

    action = None # override this with the action type this actor is about
    
    def __init__(self, *args, **kwds):
        super(Actor, self).__init__(*args, **kwds)
        self.element = self.action
        return
    

#version
__id__ = "$Id$"

# End of file 
