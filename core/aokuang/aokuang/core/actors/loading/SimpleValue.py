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


"""
This is the actor responsible for one demo of "loading" action
that shows how to load a simple value from the controller.

Note to developer: 
  one needs to subclass ....DemoPanelActor.Actor
  and implement method "createDemoPanel".
"""

import luban

from ....DemoPanelActor import Actor as base
class Actor(base):

    title='load a simple value'
    description=[
        'A simple value can be loaded from the controller and used to',
        'update the UI.',
        ]
    

    def createDemoPanel(self, **kwds):
        container = luban.e.document(title="hey")
        p1 = container.paragraph(
            text='the text to replace', 
            id='load_example1_toreplace',
            )
        # create a button
        b1 = container.button(label = 'click me', id='load_example1_button')
        # Here we set the "onclick" handler of the button to an action,
        # which will be performed when the button is clicked.
        # The action is to select the paragraph element defined above
        # and replace it with a text string loaded from
        # routine "onloadsimplevalue" of this actor.
        b1.onclick = luban.a.select(element = p1).replaceContent(
            newcontent = luban.a.load(
                actor = self.name, 
                routine = 'onloadsimplevalue')
            )
        return container

    
    def onloadsimplevalue(self, **kwds):
        return 'newvalue'
    

# End of file 

