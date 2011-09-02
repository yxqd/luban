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


class ControllerBase:


    def __init__(self, actor_package):
        if not actor_package:
            raise ValueError("must provide actor package name")
        self.actor_package = actor_package
        return
    

    def run(self, actor=None, routine=None, **kwds):
        actor = actor or 'default'
        actor = self._retrieveActor(actor)
        obj = actor.perform(routine=routine, **kwds)
        return obj


    def _retrieveActor(self, actor):
        actor_name = actor
        mod_name = '%s.%s' % (self.actor_package, actor_name)
        actor_module = __import__(
            mod_name, 
            fromlist=[''],
            )
        factory = actor_module.Actor
        if not hasattr(factory, 'expose') or not factory.expose:
            raise RuntimeError("actor %s not exposed" % factory)
        
        actor = factory()
        actor.name = actor_name
        actor.director = self
        return actor



# End of file 

