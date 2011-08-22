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
        from luban.ui.elements.Frame import Frame
        if isinstance(specification, Frame):
            return self.obj2html.render(specification)
        return self.obj2json.render(specification)

    
# End of file 
