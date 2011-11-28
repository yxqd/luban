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

    title='A trivial dialog'
    description = [
        "Please note that dialog should be only added into the frame. ",
        ]
    rank = 102
    

    def createDemoPanel(self, **kwds):
        # create dialog
        dialog = luban.e.dialog(
            title='title of dialog', 
            autoopen=True, 
            id='dialog-basic2',
            )
        # .. add a paragraph
        dialog.paragraph(text='content of dialog')
        # .. add a button
        okbutton = dialog.button(
            label='OK',
            onclick=luban.a.select(id='dialog-basic2', type='dialog').destroy()
            )
        
        # add a button that when clicked, add the dialog to the frame
        # select(id='') selects the frame
        button = luban.e.button(
            label='click me to open the dialog',
            onclick=luban.a.select(id='').append(newelement=dialog),
            )
        
        return button


# End of file 
