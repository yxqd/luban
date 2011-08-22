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


import luban.ui as lui


class ActorRetrieverMixin:

    
    def _retrieveActor(self, name):
        try:
            type = getattr(lui.e, name)
        except:
            try:
                type = getattr(lui.a, name)
            except:
                type = None

        if type is None: 
            return super()._retrieveActor(name)
        
        # actor factory
        f = type.aokuang_actor_factory
        if not hasattr(f, 'expose') or not f.expose:
            raise RuntimeError("actor %s not exposed" % f)
        
        # actor
        actor = f()
        actor.name = name
        actor.director = self
        
        return actor


    pass # end of ActorRetrieverMixin


# End of file 

