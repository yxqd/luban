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
    def index(self):
        
        actor_module = __import__(
            "Actor", fromlist=[self.actor_package]
            )
        actor = actor_module.Actor
        
        return self.weaver.weave(obj)



# End of file 

