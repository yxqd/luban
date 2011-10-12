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

    title='load a new UI element'
    description=[
        'A UI element can be loaded from the controller,',
        'to replace a part of the existing UI.',
        ]
    
    rank = 100

    def createDemoPanel(self, **kwds):
        container = luban.e.document(id='container')
        doc = container.document(title = 'the document to replace')
        button = container.button(label = 'click me', id='load_example2_button')
        # Here we set the "onclick" handler of the button to an action,
        # which will be performed when the button is clicked.
        # The action is to select the document element defined above
        # and replace it with a document loaded from
        # routine "onloadnewdocument" of this actor.
        button.onclick = luban.a.select(element = container).replaceContent(
            newcontent = luban.a.load(
                actor = self.name, 
                routine = 'onloadnewdocument',
                )
            )
        return container


    def onloadnewdocument(self, **kwds):
        newdoc = luban.e.document(title='new document')
        return newdoc
    

# End of file 

