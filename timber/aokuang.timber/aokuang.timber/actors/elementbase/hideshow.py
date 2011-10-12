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

    title='hide and show'
    description = [
        'actions to hide and show an element'
        ]
    rank = 10006
    
    def createDemoPanel(self, **kwds):
        container = luban.e.document()
        
        doc = container.document(
            title = 'the document to show/hide', 
            id=luban.uuid())
        
        b1 = container.button(label = 'click to hide')
        b1.onclick = luban.a.select(element = doc).hide()
        
        b2 = container.button(label = 'click to show')
        b2.onclick = luban.a.select(element = doc).show()
        
        return container
    


# End of file 
