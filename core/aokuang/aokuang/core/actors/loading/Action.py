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

    title='load an action'
    description=[
        'In this example, an action is loaded from the controller,',
        'and the loaded action is then executed.',
        'The loaded action is adding a class to a document.',
        ]

    def createDemoPanel(self, **kwds):
        container = lui.e.document()
        doc = container.document(
            title = 'The document to change',
            id = 'document-to-change',
            )
        button = container.button(label = 'click me', id='load_example3_button')
        # click the button will load from routine onloadaction of this actor.
        # since the loaded is an action, that action will then be performed.
        button.onclick = lui.a.load(actor = self.name, routine = 'onloadaction')
        return container
    
    
    def onloadaction(self, **kwds):
        # select the element (note keyword id is used to construct the selector)
        # and then add a class "green-border".
        # In web application, this class is rendered as css class,
        # the ".green-border" was defined to have a green border in
        # aokuang.css
        return lui.a.select(id='document-to-change')\
            .addClass(cls='green-border')


# End of file 

