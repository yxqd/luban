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

from luban import ui as lui

from ....DemoPanelActor import Actor as base
class Actor(base):

    title='load a new UI element'
    description=[
        'A UI element can be loaded from the controller,',
        'to replace a part of the existing UI.',
        ]


    def createDemoPanel(self, **kwds):
        container = lui.e.document(id='container')
        doc = container.document(title = 'the document to replace')
        button = container.button(label = 'click me', id='load_example2_button')
        # Here we set the "onclick" handler of the button to an action,
        # which will be performed when the button is clicked.
        # The action is to select the document element defined above
        # and replace it with a document loaded from
        # routine "onloadnewdocument" of this actor.
        button.onclick = lui.a.select(element = container).replaceContent(
            newcontent = lui.a.load(
                actor = self.name, 
                routine = 'onloadnewdocument',
                )
            )
        return container


    def onloadnewdocument(self, **kwds):
        newdoc = lui.e.document(title='new document')
        return newdoc
    

# End of file 

