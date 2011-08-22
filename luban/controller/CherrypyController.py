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

    def __init__(self, url, static_html_base='static', actor_package=None):
        
        self.url = url
        self.static_html_base = static_html_base

        if not actor_package:
            raise ValueError("must provide actor package name")
        self.actor_package = actor_package
        
        from luban.weaver.web import create as createWeaver
        self.weaver = createWeaver(
            controller_url = url,
            statichtmlbase=static_html_base)
        return
    

    @cherrypy.expose
    def index(self, actor=None, routine=None, **kwds):
        if not actor:
            raise RuntimeError
        
        actor_name = actor
        mod_name = '%s.%s' % (self.actor_package, actor_name)
        actor_module = __import__(
            mod_name, 
            fromlist=[''],
            )
        actor = actor_module.Actor()
        actor.name = actor_name
        actor.director = self
        
        obj = actor.perform(routine=routine, **kwds)
        return self.weaver.weave(obj)



# End of file 

