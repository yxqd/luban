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

    title='select_dialog.replaceContent(newcontent=...)'
    description = [
        "replace content of a dialog",
        ]
    rank = 201
    

    def createDemoPanel(self, **kwds):
        # create dialog
        dialog = luban.e.dialog(
            title='title of dialog', 
            autoopen=True, 
            id='dialog-replacecontent',
            )
        # .. add a paragraph
        dialog.paragraph(text='content of dialog')
        
        # .. the close button. this is only added when the next button click
        okbutton = luban.e.button(
            label='Close',
            onclick=luban.a.select(element=dialog).destroy()
            )
        
        # .. add a button when click replace the content of the dialog
        # .. with the close button
        repl_button = dialog.button(
            label = 'click me',
            onclick = luban.a.select(element=dialog).replaceContent(
                newcontent = okbutton),
            )
        
        # add a button that when clicked, add the dialog to the frame
        # select(id='') selects the frame
        button = luban.e.button(
            label='click me to open the dialog',
            onclick=luban.a.select(id='').append(newelement=dialog),
            )
        
        return button


# End of file 
