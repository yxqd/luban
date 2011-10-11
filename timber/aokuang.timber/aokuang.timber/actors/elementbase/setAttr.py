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

    title='setAttr'
    description = [
        'action to change attributes of an element',
        ]
    rank = 10004
    
    def createDemoPanel(self, **kwds):
        container = luban.e.document()

        textfield = container.formtextfield(label='text', value='value', id=luban.uuid())
        
        button = container.button(label = 'click me')
        button.onclick = luban.a.select(element = textfield).setAttr(
            label = 'new text',
            value = 'new value',
            )
        return container
    


# End of file 
