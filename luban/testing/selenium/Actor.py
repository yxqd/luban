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


from ..ActorBase import Actor as ActorBase

class Actor(ActorBase):


    from Selector import Selector

    
    def __init__(self, selenium):
        self.selenium = selenium
        return


    def getAlert(self):
        return self.selenium.get_alert()


    def select(self, id=None, type=None, **kwds):
        s = super(Actor, self).select(id=id, type=type, **kwds)
        s.selenium = self.selenium
        return s

    
    def __del__(self):
        self.selenium.stop()
        return
    


# version
__id__ = "$Id$"

# End of file 

