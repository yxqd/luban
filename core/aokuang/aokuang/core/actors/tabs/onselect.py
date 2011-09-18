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

    title='"onselect" event'
    description = [
        ]
    def createDemoPanel(self, **kwds):
        tabs = luban.e.tabs()
        tab1 = tabs.tab(label="tab1", id='tab1')
        tab2 = tabs.tab(label="tab2", id='tab2')
        show_change = luban.a.load(
            actor=self.name, routine='onchangetab',
            old = luban.event.oldtab,
            new = luban.event.newtab,
            )
        tab1.onselect = tab2.onselect = show_change
        return tabs


    def onchangetab(self, old=None, new=None, **kwds):
        msg = "tab switched from %r to %r" % (old, new)
        return luban.a.alert(msg)


# End of file 
