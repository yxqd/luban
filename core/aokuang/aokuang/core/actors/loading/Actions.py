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

    title='load two actions'
    description=[
        'In this example, two actions are loaded from the controller in one call,',
        'and the loaded actions are then executed.',
        'The loaded actions: adding a class to a document and an alert.',
        ]

    def createDemoPanel(self, **kwds):
        container = luban.e.document()
        doc = container.document(
            title = 'The document to change',
            id = 'loading-actions-document-to-change',
            )
        button = container.button(label = 'click me', id='load_actions_button')
        # click the button will load from routine onloadaction of this actor.
        button.onclick = luban.a.load(actor = self.name, routine = 'onloadaction')
        return container
    
    
    def onloadaction(self, **kwds):
        # return two actions in a list
        # both actions will be performed
        return [
            luban.a.select(id='loading-actions-document-to-change')\
                .addClass(cls='green-border'),
            luban.a.alert("document class changed"),
            ]


# End of file 

