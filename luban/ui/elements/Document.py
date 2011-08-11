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
from .SimpleContainer import SimpleContainer, Meta

class Document(DocumentFactory, ParagraphFactory, SimpleContainer, metaclass=Meta):

    simple_description = 'A simple element container with a title'
    full_description = (
        "Document is a simple element container. "
        "Instances of most widget types can be children of a document. "
        "A document widget has a title which can be empty. "
        )
    
    abstract = False

    def document(self, **kwds):
        document = Document(**kwds)
        self.append(document)
        return document


    def identify(self, inspector):
        return inspector.onDocument(self)


    title = descriptors.str()
    title.tip = 'Title of the document'
    


from .Frame import Frame
Document.disallowed_element_types = [Frame]
del Frame


# version
__id__ = "$Id$"

# End of file
