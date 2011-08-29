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

import luban.ui as lui

from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    
    def default(self):
        return self.frame()
    

    def frame(self):
        frame = lui.e.frame(title="luban test: tabs")
        doc = frame.document(title="Tabs")
        tabs = doc.tabs()
        tab1 = tabs.tab(label="tab1")
        tab2 = tabs.tab(label="tab2")
        tab1.onselect = lui.a.load(
            actor=self.name, routine='onchangetab',
            old = lui.event.oldtab,
            new = lui.event.newtab,
            )
        return frame


    def onchangetab(self, **kwds):
        return lui.a.alert(str(kwds))



# End of file 

