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
from .SimpleContainer import SimpleContainer


class Document(DocumentFactory, ParagraphFactory, LinkFactory, SimpleContainer):

    simple_description = 'A simple element container with a title'
    full_description = (
        "Document is a simple element container. "
        "Instances of most widget types can be children of a document. "
        "A document widget has a title which can be empty. "
        )
    
    abstract = False

    def splitter(self, **kwds):
        from .Splitter import Splitter as factory
        element = factory(**kwds)
        self.append(element)
        return element


    def form(self, **kwds):
        from .Form import Form
        form = Form(**kwds)
        self.append(form)
        return form


    def document(self, **kwds):
        #from Document import Document
        document = Document(**kwds)
        self.append(document)
        return document


    def identify(self, inspector):
        return inspector.onDocument(self)


    title = descriptors.str()
    title.tip = 'Title of the document'
    
    collapsable = descriptors.bool()
    collapsable.tip = 'If true, the document will have a collapse/expand control and it will be collapsable'
    
    collapsed = descriptors.bool()
    collapsed.tip = 'If true, the document is collapsed initially. "collapsable" must be true for this option to work'
    dockable = descriptors.bool()
    dockable.tip = 'If true, the document will have a "dock" control. By clicking the "dock" control, a user can minimize the document to the dock. For this option to work, a "dock" widget must have already existed in your application frame.'
    
    closable = descriptors.bool()
    closable.tip = 'If true, the document will have a "close" control which, when clicked, will close (destroy) the document'

    # following are in effect only if collapsable is True
    onexpand = descriptors.action()
    onexpand.tip = 'action on event "expand". The "expand" event happens when a user expand the document. Only valid if the document is collapsable'
    oncollapse = descriptors.action()
    oncollapse.tip = 'action on event "collapse". The "collapse" event happens when a user collapse the document. Only valid if the document is collapsable'
    


from .Frame import Frame
Document.disallowed_element_types = [Frame]
del Frame


# version
__id__ = "$Id$"

# End of file
