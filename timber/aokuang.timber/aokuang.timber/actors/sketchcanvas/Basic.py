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

    title='Basic demo'
    description = [
        ]

    def createDemoPanel(self, **kwds):
        onsave = luban.a.load(
            actor=self.name, routine='onSave',
            data = luban.event.data,
            )
        return luban.e.sketchcanvas(
            onsave = onsave,
            # autosave=30 # comment this out for auto-saving every half min
            )


    def onSave(self, data=None, **kwds):
        print ("saving")
        from luban.timber.elements.SketchCanvas import todata
        data = todata(data)

        import os
        tmpdir = 'tmp'
        if not os.path.exists(tmpdir): os.makedirs(tmpdir)

        f = os.path.join(tmpdir, 'saved-sketch.png')
        open(f, 'wb').write(data)
        return



# End of file 
