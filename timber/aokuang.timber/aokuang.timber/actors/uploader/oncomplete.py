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

import luban

from ....DemoPanelActor import Actor as base
class Actor(base):

    title='"oncomplete" and "onfail" event'
    description = [
        ]

    def createDemoPanel(self, **kwds):
        from luban import uuid
        uploadid = str(uuid.uuid())
        # create uploader
        oncomplete = luban.a.load(
            actor=self.name, routine='onUpload', 
            filename=luban.event.filename,
            uploadid = uploadid,
            )
        onfail = luban.a.alert(luban.event.reason)
        uploader = luban.e.uploader(
            label='Upload',
            id = uploadid,
            oncomplete = oncomplete,
            onfail = onfail,
            )
        return uploader


    def onUpload(self, filename=None, uploadid=None, **kwds):
        fpath = self.controller._getUploadFilePath(filename, uploadid)
        import os
        assert os.path.exists(fpath)
        # now we should move the uploaded file to some long term
        # storage 
        # but we will skip that
        import os
        size = os.path.getsize(fpath)
        title="uploaded file: filename=%s, size=%s" % (filename, size)
        doc = luban.e.document(title = title)
        return luban.a.select(id=uploadid).replaceBy(newelement=doc)


# End of file 
