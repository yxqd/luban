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


class Controller(object):

    def __getattr__(self, k):
        actor = Actor(k)
        return actor



class Actor(object):

    def __init__(self, name):
        super(Actor, self).__init__()
        self.name = name


    def __getattr__(self, k):
        method = Method(k, actor=self.name)
        return method



class Method(object):


    def __init__(self, name, actor):
        super(Method, self).__init__()
        self.name = name
        self.actor = actor
        self._called = False
        return
    
    
    def __call__(self, **kwds):
        if self._called: raise RuntimeError, 'can only be called once'
        self.kwds = kwds
        self._called = True
        return


    def identify(self, visitor):
        return visitor.onCallingActorMethod(self)
    

# version
__id__ = "$Id$"

# End of file 
