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

    title='A basic progressbar'
    description = [
        ]


    def createDemoPanel(self, **kwds):
        self.setProgress(0)
        pb = luban.e.progressbar(id='pbar')
        pb.onchecking = luban.a.load(actor=self.name, routine='check')
        pb.onfinish = luban.a.load(actor=self.name, routine='done')
        return pb


    def check(self, **kwds):
        # this is only a demo implementation.
        # for a real useful progressbar, it should be watching
        # progress of a task running on the server side.
        status = 'working...'
        p = self.getProgress()
        p += 10
        if p>=100:
            p=100
            status = 'done.'
        self.setProgress(p)
        return luban.a.select(id='pbar').setAttr(
            percentage = p, status = status)


    def done(self, **kwds):
        return luban.a.alert('done')


    filename = 'testprogressbar.dat'
    def setProgress(self, value):
        open(self.filename, 'w').write(str(value))
        return
    def getProgress(self):
        filename = self.filename
        import os
        if not os.path.exists(filename): return 0
        return int(open(filename).read())


# End of file 
