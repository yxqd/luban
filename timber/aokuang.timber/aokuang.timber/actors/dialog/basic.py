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

    title='A dialog'
    description = [
        ]
    rank = 100
    

    def createDemoPanel(self):
        document = luban.e.document(id='container')
        
        # create dialog
        dialog = document.dialog(
            title='title of dialog', 
            autoopen=True, 
            id='dialog-basic',
            )
        # add a paragraph
        dialog.paragraph(text='content of dialog')

        # add a button
        okbutton = dialog.button(
            label='OK',
            onclick=luban.a.select(element=dialog).destroy()
            )
        
        # add a button to open the dialog
        button = document.button(
            label='click me to open a dialog',
            onclick=luban.a.select(element=document).append(newelement=dialog),
            )
        
        return document


# End of file 
