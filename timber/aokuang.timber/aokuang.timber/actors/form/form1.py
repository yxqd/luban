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

    title='A form with one text field'
    description = [
        ]
    def createDemoPanel(self, **kwds):
        form = luban.e.form(title='login')
        username = form.text(label='username')
        username.onchange = luban.a.load(
            actor=self.name, routine='onchange',
            old = luban.event.old, new = luban.event.new
            )
        return form


    def onchange(self, old=None, new=None, **kwds):
        return luban.a.alert("value changed from %r to %r" % (old, new))


# End of file 
