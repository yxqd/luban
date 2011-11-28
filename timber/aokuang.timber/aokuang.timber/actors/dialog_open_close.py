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
url examples:

 http://localhost:22346/dialog_open_close
"""


import luban


from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    def default(self, **kwds):
        frame = luban.e.frame(title='dialog demo')

        # dialog
        dialog = self._createDialog()
        frame.append(dialog)
        
        # doc
        text  = (
            "Dialog could be added on demand, and destoryed (shown in the main aokuang interface)."
            "It could also exists from the start until the frame is replaced, "
            "but only shows up when necessary. "
            "This is what is shown in this demo."
            )
        doc = frame.document()
        doc.paragraph(text = text)
        # add a button to open the dialog
        button = doc.button(
            label='click me to show the dialog',
            id = 'opendialog-button',
            onclick=luban.a.select(element=dialog).open(),
            )

        # another button to check dialog can be destroy correctly
        newframe = luban.e.frame(); 
        newframe.append(button) # intentionally leave the button in. this button won't work
        newframe.oncreate = luban.a.select(element=button).setAttr(label='open dialog: this should be not working')
        
        button2 = doc.button(
            label = 'click me to replace the content of the frame to a new frame without dialog',
            onclick = luban.a.select(id='').replaceBy(newelement=newframe)
            )
        
        return luban.a.establishInterface(frame)


    def _createDialog(self):
        # create dialog
        dialog = luban.e.dialog(
            title='title of dialog', 
            autoopen=False, 
            id='dialog-basic',
            )
        # add a paragraph
        dialog.paragraph(text='content of dialog')

        # add a button
        okbutton = dialog.button(
            label='OK',
            onclick=luban.a.select(element=dialog).close()
            )
        return dialog
        


# End of file 
