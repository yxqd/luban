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
tabs
"""

import luban

from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    
    def default(self):
        return self.frame()
    

    def frame(self):
        frame = luban.e.frame(title="luban test: tabs")
        doc = frame.document(title="Tabs")
        tabs = doc.tabs()
        tab1 = tabs.tab(label="tab1", id='tab1')
        tab2 = tabs.tab(label="tab2", id='tab2')
        tab1.onselect = luban.a.load(
            actor=self.name, routine='onchangetab',
            old = luban.event.oldtab,
            new = luban.event.newtab,
            )
        return frame


    def onchangetab(self, old=None, new=None, **kwds):
        msg = "tab switched from %r to %r" % (old, new)
        return luban.a.alert(msg)


    def onchangetab_debug(self, **kwds):
        return luban.a.alert(str(kwds))



# End of file 

