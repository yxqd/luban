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

    title='actions about "Class"'
    description = [
        "click buttons to see effects.",
        ]
    rank = 10002
    
    def createDemoPanel(self, **kwds):
        container = luban.e.document()
        # document to be affected
        doc = container.document(
            title = 'The document to change',
            id = 'document-to-change',
            )
        # button1
        button = container.button(label = 'click me to add green border')
        button.onclick = luban.a.select(element=doc).addClass(cls='green-border')
        # button2
        button = container.button(label = 'click me to remove green border')
        button.onclick = luban.a.select(element=doc).removeClass(cls='green-border')
        
        return container
    


# End of file 
