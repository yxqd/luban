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

    title='multiple uploads'
    description = [
        ]

    def createDemoPanel(self, **kwds):
        uploadid = str(luban.uuid())
        # create uploader
        oncomplete = luban.a.load(
            actor=self.name, routine='onUpload', 
            filenames=luban.event.filenames,
            uploadid = uploadid,
            )
        onfail = luban.a.alert(luban.event.reason)
        uploader = luban.e.uploader(
            label='Upload',
            id = uploadid,
            oncomplete = oncomplete,
            onfail = onfail,
            multiple = True,
            )
        return uploader


    def onUpload(self, filenames=None, uploadid=None, **kwds):
        filenames = filenames.split(',')
        import os
        doc = luban.e.document()
        # now we could move the uploaded file to some long term
        # storage 
        # but we will skip that
        for filename in filenames:
            fpath = self.controller._getUploadFilePath(filename, uploadid)
            assert os.path.exists(fpath), "%s does not exist" % fpath
            size = os.path.getsize(fpath)
            text="uploaded file: filename=%s, size=%s" % (filename, size)
            doc.paragraph(text=text)
            continue
        return luban.a.select(id=uploadid).replaceBy(newelement=doc)


# End of file 
