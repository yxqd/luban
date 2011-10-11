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

    title='replaceBy'
    description = [
        'action to replace a UI element (hierarchy) with a new one'
        ]
    rank = 10003
    
    def createDemoPanel(self, **kwds):
        container = luban.e.document(id='container')
        
        doc = container.document(title = 'the document to replace', id=luban.uuid())
        newdoc = luban.e.document(title = 'new document')
        
        button = container.button(label = 'click me')
        button.onclick = luban.a.select(element = doc).replaceBy(newelement = newdoc)
        return container
    


# End of file 
