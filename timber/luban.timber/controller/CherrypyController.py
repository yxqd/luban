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


# in addition to the controller in luban core, the following are added
#
# 1. session
#   this is not realy used yet. need to think more about this.
#   do we really need it?
# 2. upload
#   this is done pretty ad hoc
#   the blueimp file upload js lib is used
#   the upload progress is done by server writing done the progress info
#   in a little file, and then on the client side every second
#   a request will be sent to update how much have been uploaded




from luban.controller.CherrypyController import CherrypyController as base
from .CherrypyUploadHandler_Mixin import Mixin as UploadMixin
class CherrypyController(UploadMixin, base):

    pass


# borrow cherrypy session as luban session
class SessionProxy:

    def _luban_session_handle(self):
        import cherrypy
        return cherrypy.session
    
    def __getattr__(self, key):
        h = self._luban_session_handle()
        return getattr(h, key)

    def __setitem__(self, k, v):
        h = self._luban_session_handle()
        return h.__setitem__(k,v)

    def __getitem__(self, k):
        h = self._luban_session_handle()
        return h[k]
import luban
luban.session = SessionProxy()


# borrow thread specific data container from cherrypy
import cherrypy
luban.thread_data = cherrypy.thread_data

# overload the luban core controller
import luban.controller.CherrypyController as core_CherrypyController_module
core_CherrypyController_module.CherrypyController = CherrypyController


# End of file 

