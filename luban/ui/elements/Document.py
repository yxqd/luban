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


"""
Document

An example of a simple container UI element.
"""


from .DocumentFactory import DocumentFactory
from .ParagraphFactory import ParagraphFactory
from .SimpleContainer import SimpleContainer, Meta

class Document(SimpleContainer, metaclass=Meta):

    simple_description = 'A simple element container with a title'
    full_description = (
        "Document is a simple element container. "
        "Instances of most widget types can be children of a document. "
        "A document widget has a title which can be empty. "
        )
    
    abstract = False

    # attributes
    title = descriptors.str()
    title.tip = 'Title of the document'
    
    # for inspector
    def identify(self, inspector):
        return inspector.onDocument(self)



# version
__id__ = "$Id$"

# End of file
