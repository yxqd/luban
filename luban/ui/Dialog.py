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


from .DocumentFactory import DocumentFactory
from .ParagraphFactory import ParagraphFactory
from .LinkFactory import LinkFactory
from .SimpleContainer import SimpleContainer as elembase


class Dialog(DocumentFactory, ParagraphFactory, LinkFactory, elembase):

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
    
    abstract = False

    autoopen = elembase.descriptors.bool(name='autoopen', default=False)
    autoopen.tip = 'If true, the dialog is opened when created'
    
    title = elembase.descriptors.str(name='title')
    title.tip = 'Title of the dialog'

    def identify(self, inspector):
        return inspector.onDialog(self)


class DialogActions(object):


    def dialog(self, actionname, **kwds):
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)


# version
__id__ = "$Id$"

# End of file
