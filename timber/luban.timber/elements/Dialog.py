#!/usr/bin/env python
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



from luban.ui.elements.SimpleContainer import SimpleContainer, Meta
class Dialog(SimpleContainer, metaclass=Meta):

    # decorations
    simple_description = 'A dialog that is a container of luban elements'
    full_description = (
        "A dialog is a simple element container that floats. "
        "In luban, all dialogs are modal; you can create non-modal windows "
        "by 'dockable documents', please refer to the 'document' element "
        "for more details. "
        "Instances of most widget types can be children of a dialog. "
        "A dialog usually has a title, and you should usually add an 'OK' "
        "or 'Close' button to close it."
        )

    # properties
    autoopen = descriptors.bool()
    autoopen.tip = 'If true, the dialog is opened when created'
    
    title = descriptors.str()
    title.tip = 'Title of the dialog'

    # methods
    def identify(self, inspector):
        return inspector.onDialog(self)


# actions
# to define a new element action, subclass ElementActionBase
from luban.ui.actions.ElementActionBase import ElementActionBase
class DialogOpen(ElementActionBase):
    
    "open a dialog"
    
    # decorations
    element_type = Dialog
    factory_method = "open"
    
    # methods
    def identify(self, visitor):
        return visitor.onDialogOpen(self)

class DialogClose(ElementActionBase):

    "close a dialog"
      
    # decorations
    element_type = Dialog
    factory_method = "close"
    
    # methods
    def identify(self, visitor):
        return visitor.onDialogClose(self)


# End of file
