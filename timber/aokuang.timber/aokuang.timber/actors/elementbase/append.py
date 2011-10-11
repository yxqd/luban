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

    title='append'
    description = [
        'action to append a new element to a selected element'
        ]
    rank = 10004
    
    def createDemoPanel(self, **kwds):
        container = luban.e.document(id='container')
        
        doc = container.document(
            title = 'the document to which a new element will be appended', 
            id=luban.uuid())
        
        newelem = luban.e.paragraph(text = 'new element')
        
        button = container.button(label = 'click me')
        button.onclick = luban.a.select(element = doc).append(newelement = newelem)
        return container
    


# End of file 
