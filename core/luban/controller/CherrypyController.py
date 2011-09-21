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

    
    upload_limit = 1000*1024*1024 # 10M
    upload_timeout = 60000 # 10 minutes
    @cherrypy.expose
    @cherrypy.tools.json_out(content_type="text/html")
    def upload(self, myfile):
        cherrypy.response.timeout = self.upload_timeout
        size = 0
        while True:
            data = myfile.file.read(8192)
            if not data:
                break
            size += len(data)
            if size > self.upload_limit:
                raise cherrypy.HTTPError(413)
            continue
                
        return [{
            "name": myfile.filename,
            "size": size,
            "type": str(myfile.content_type),
            }]


# End of file 

