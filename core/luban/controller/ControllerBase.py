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


class ControllerBase(object):


    def __init__(
        self,
        actor_package=None, actor_packages=None,
        default_actor="start",
        ):
        
        if not actor_package and not actor_packages:
            raise ValueError("must provide actor package name")
        if actor_package and actor_packages:
            raise ValueError("confused: both actor_package and actor_packages are provided")
        if actor_package:
            actor_packages = [actor_package]
        self.actor_packages = actor_packages

        self.default_actor = default_actor
        return
    

    def call(self, actor=None, routine=None, *args, **kwds):
        actor = actor or self.default_actor
        actor = self._retrieveActor(actor)
        obj = actor.perform(routine, *args, **kwds)
        return obj


    def _retrieveActor(self, actor):
        exceptions = []
        for package in self.actor_packages:
            try:
                return self._retrieveActor1(actor, package)
            except Exception as e:
                import traceback
                tb = traceback.format_exc()
                exceptions.append((e,tb))
                pass
            continue
        msg = "unable to retrieve actor %s from %s. " % (actor, self.actor_packages)
        msg += "forgot to export the actor?\n"
        msg += "\nExceptions:\n"
        for e, tb in exceptions:
            msg += str(e) + "\n"
            msg += "traceback: %s\n\n" % tb
        raise RuntimeError(msg)


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

