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

"""
weaver that renders response from luban ui objects

weaver = Weaver()
# customize obj->dict converter
weaver.obj2json.obj2dict = MyObj2Dict()
# weave
weaver.weave(luban_obj)
"""


impl = """

"use" relations

weaver 
 + obj2json
 + obj2html
   + frame2htmldoc
     + obj2json

"""


class Weaver:


    def __init__(self):
        # obj->html
        from .HtmlRenderer import HtmlRenderer
        self.obj2html = HtmlRenderer()

        # obj->json
        from .JsonReprRenderer import JsonReprRenderer
        self.obj2json = JsonReprRenderer()
        return


    @property
    def obj2json(self): return self._obj2json
    @obj2json.setter
    def obj2json(self, obj2json):
        self._obj2json = obj2json
        self.obj2html.obj2json = obj2json
        return obj2json
    

    def weave(self, specification):
        """create output from the given UI specification
        """
        from luban.ui.actions.EstablishInterface import EstablishInterface
        if isinstance(specification, EstablishInterface):
            return self.obj2html.render(specification)
        return self.obj2json.render(specification)

    
    def use_library_bundle(self, bundle):
        '''make use of the given library 
        a library contains information regarding javascript module
        and css module for luban base, widgets, and the application

        * library: an object. each attribute of the object needs 
          to be a dictionary 
          of {'stylesheets': <list>, 'javascripts': <list>}
        '''
        bundle = bundle or self.default_bundle
        for name in dir(bundle):
            if name.startswith('_'): continue
            libs = getattr(bundle, name)
            self.obj2html.librarian.register(name, libs)
            continue
        return
    from .libraries.default import bundle as default_bundle


    def customize_application(self, stylesheets=None, javascripts=None):
        """tell the weaver where to find the css modules
        specific for the current application
        """
        from .Library import Library
        Library('app', css=stylesheets, javascripts=javascripts, replace=True)
        self.obj2html.librarian.register('application', ['app'])
        return


# End of file 
