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


from .WebAppController import WebAppController
class CherrypyController(WebAppController):
    
    @cherrypy.expose
    def index(self, actor=None, routine=None, **kwds):
        return self.run(actor=actor, routine=routine, **kwds)

    
    @cherrypy.expose
    @cherrypy.tools.json_out(content_type="text/html")
    def upload(self, myfile):
        s = myfile.file.read()
        return [{
            "name": "name",
            "size": len(s),
            "type": "text",
            }]


# End of file 

