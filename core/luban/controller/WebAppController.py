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


from .ControllerBase import ControllerBase
class WebAppController(ControllerBase):

    stylesheets = []
    javascripts = []

    def __init__(
        self, url,
        static_html_base='static', 
        actor_package=None,
        stylesheets = None, javascripts = None,
        web_weaver_library = None,
        ):
        # init bases
        super().__init__(actor_package)
        
        #
        self.url = url
        self.static_html_base = static_html_base
        
        # weaver
        from luban.weaver.web import create as createWeaver
        weaver = self.weaver = createWeaver(
            controller_url = url,
            statichtmlbase=static_html_base)
        # in case a custom web weaver library is supplied
        # use it
        if web_weaver_library:
            weaver.use_library(web_weaver_library)

        #
        stylesheets = stylesheets or self.stylesheets or []
        javascripts = javascripts or self.javascripts or []
        if stylesheets or javascripts:
            weaver.customize_application(
                stylesheets = stylesheets, 
                javascripts = javascripts)
        return
    

    def run(self, actor=None, routine=None, **kwds):
        obj = super().run(actor=actor, routine=routine, **kwds)
        return self.weaver.weave(obj)



# End of file 

