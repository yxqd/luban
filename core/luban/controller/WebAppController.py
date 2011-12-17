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
        html_base='',  # base url of the site
        static_html_base='static',  # html_base/static_html_base gives the url of the static html root
        stylesheets = None, javascripts = None,
        web_weaver_library = None,
        #
        actor_package=None, actor_packages=None,
        **kwds
        ):
        # init bases
        super().__init__(
            actor_package=actor_package,
            actor_packages=actor_packages,
            **kwds)
        
        #
        self.url = url
        self.html_base = html_base
        self.static_html_base = static_html_base
        
        # weaver
        from luban.weaver.web import create as createWeaver
        weaver = self.weaver = createWeaver(
            htmlbase = html_base,
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
    

    def run(self, actor=None, routine=None, *args, **kwds):
        obj = self.call(actor, routine, *args, **kwds)
        return self.weaver.weave(obj)



# End of file 

