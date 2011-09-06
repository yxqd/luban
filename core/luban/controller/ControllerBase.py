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
    

    def call(self, actor=None, routine=None, **kwds):
        actor = actor or 'default'
        actor = self._retrieveActor(actor)
        obj = actor.perform(routine=routine, **kwds)
        return obj


    def _retrieveActor(self, actor):
        actor_name = actor
        tokens = actor_name.split('.')

        if len(tokens) > 1:
            pkg = self.actor_package + '.' + '.'.join(tokens[:-1])
            module = tokens[-1]
        else:
            pkg = self.actor_package
            module = actor_name            
        from ..utils.importer import import_module
        actor_module = import_module(module, pkg=pkg)
        
        factory = actor_module.Actor
        if not hasattr(factory, 'expose') or not factory.expose:
            raise RuntimeError("actor %s not exposed" % factory)
        
        actor = factory()
        actor.name = actor_name
        actor.controller = self
        return actor



# End of file 

