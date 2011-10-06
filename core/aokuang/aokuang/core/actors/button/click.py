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

    title='"click" action'
    description = [
        'Programmically click a button',
        ]
    def createDemoPanel(self, **kwds):
        doc = luban.e.document(id='container')
        b1 = doc.button(
            id = 'b1',
            label = 'a button', 
            onclick = luban.a.alert("button 1 clicked"),
            )
        b2 = luban.e.button(
            label = 'click me',
            onclick = luban.a.select(element=b1).click(),
            )
        return button


# End of file 
