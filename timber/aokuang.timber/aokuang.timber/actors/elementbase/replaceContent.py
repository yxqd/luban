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

    title='replaceContent'
    description = [
        'action to replace the interior of a UI element a new element'
        ]
    rank = 10004
    
    def createDemoPanel(self, **kwds):
        container = luban.e.document()
        
        doc = container.document(
            title = 'the document for which the interior with be replaced', 
            id=luban.uuid())
        doc.paragraph(text='interior')
        
        newdoc = luban.e.document(title = 'new interior')
        
        button = container.button(label = 'click me')
        button.onclick = luban.a.select(element = doc).replaceContent(newcontent = newdoc)
        return container
    


# End of file 
