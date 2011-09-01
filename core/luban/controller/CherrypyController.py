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


import cherrypy, luban.ui as lui

class CherrypyController:

    def __init__(
        self, url,
        static_html_base='static', 
        actor_package=None,
        web_weaver_library = None,
        ):
        
        self.url = url
        self.static_html_base = static_html_base

        if not actor_package:
            raise ValueError("must provide actor package name")
        self.actor_package = actor_package
        
        from luban.weaver.web import create as createWeaver, use_library
        weaver = self.weaver = createWeaver(
            controller_url = url,
            statichtmlbase=static_html_base)
        # in case a custom web weaver library is supplied
        # use it
        if web_weaver_library:
            use_library(web_weaver_library, weaver)
        return
    

    @cherrypy.expose
    def index(self, actor=None, routine=None, **kwds):
        actor = actor or 'default'
        actor = self._retrieveActor(actor)
        obj = actor.perform(routine=routine, **kwds)
        return self.weaver.weave(obj)


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

