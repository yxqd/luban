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


    def __init__(self, actor_package=None, actor_packages=[]):
        if not actor_package and not actor_packages:
            raise ValueError("must provide actor package name")
        if actor_package and actor_packages:
            raise ValueError("confused: both actor_package and actor_packages are provided")
        if actor_package:
            actor_packages = [actor_package]
        self.actor_packages = actor_packages
        return
    

    def call(self, actor=None, routine=None, **kwds):
        actor = actor or 'default'
        actor = self._retrieveActor(actor)
        obj = actor.perform(routine=routine, **kwds)
        return obj


    def _retrieveActor(self, actor):
        for package in self.actor_packages:
            try:
                return self._retrieveActor1(actor, package)
            except:
                pass
            continue
        raise


    def _retrieveActor1(self, actor, package=None):
        actor_name = actor
        tokens = actor_name.split('.')

        if len(tokens) > 1:
            pkg = package + '.' + '.'.join(tokens[:-1])
            module = tokens[-1]
        else:
            pkg = package
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

