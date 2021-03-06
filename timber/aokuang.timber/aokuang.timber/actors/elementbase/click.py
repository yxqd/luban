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
    rank = 10001
    
    def createDemoPanel(self, **kwds):
        doc = luban.e.document()
        b1 = doc.button(
            id = 'b1',
            label = 'this button when clicked will trigger an alert', 
            onclick = luban.a.alert("button 1 clicked"),
            )
        b2 = doc.button(
            label = 'this button when clicked will trigger the previous button to "click"',
            onclick = [
                luban.a.alert("button 2 clicked. it will trigger button 1 to click."),
                luban.a.select(element=b1).click(),
                ]
            )
        return doc


# End of file 
