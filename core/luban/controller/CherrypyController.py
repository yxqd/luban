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


import cherrypy


from .ControllerBase import ControllerBase
class CherrypyController(ControllerBase):

    def __init__(
        self, url,
        static_html_base='static', 
        actor_package=None,
        web_weaver_library = None,
        ):
        # init bases
        super().__init__(actor_package)
        
        #
        self.url = url
        self.static_html_base = static_html_base

        # weaver
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
        obj = self.run(actor=actor, routine=routine, **kwds)
        return self.weaver.weave(obj)



# End of file 

