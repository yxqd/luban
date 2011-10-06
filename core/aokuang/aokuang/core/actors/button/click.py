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
        'Programmatically click a button',
        ]
    def createDemoPanel(self, **kwds):
        doc = luban.e.document(id='container')
        b1 = doc.button(
            id = 'b1',
            label = 'a button', 
            onclick = luban.a.alert("button 1 clicked"),
            )
        b2 = doc.button(
            label = 'click me',
            onclick = [
                luban.a.alert("button 2 clicked. it will trigger button 1 to click."),
                luban.a.select(element=b1).click(),
                ]
            )
        return doc


# End of file 
