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

    
    def use_library(self, library):
        '''make use of the given library 
        a library contains information regarding javascript module
        and css module for luban base, widgets, and the application

        * library: an object. each attribute of the object needs 
          to be a dictionary 
          of {'stylesheets': <list>, 'javascripts': <list>}
        '''
        library = library or self.default_library
        for k in dir(library):
            # skip private props
            if k.startswith('_'): continue
            # 
            v = getattr(library, k)
            try:
                v.get
            except AttributeError:
                m = "%s=%r" % (k,v)
                m += "is not a valid entry in a luban web weaver library."
                m += "it must be dict-like."
                m += "The problematic library is %r" % (library,)
                raise RuntimeError(m)
            #
            stylesheets = v.get('stylesheets') or []
            javascripts = v.get('javascripts') or []
            #
            self.obj2html.librarian.register(k, stylesheets, javascripts)
            continue
        return
    from .libraries import default as default_library


    def customize_application(self, stylesheets=None, javascripts=None):
        """tell the weaver where to find the css modules
        specific for the current application
        """
        self.obj2html.librarian.register(
            'application',
            stylesheets, javascripts,
            )


# End of file 
