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


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from .SimpleContainer import SimpleContainer, Meta

class Document(SimpleContainer):

    simple_description = 'A simple element container with a title'
    full_description = (
        "Document is a simple element container. "
        "Instances of most widget types can be children of a document. "
        "A document widget has a title which can be empty. "
        )
    

    # attributes
    title = descriptors.str()
    title.tip = 'Title of the document'
    
    # for inspector
    def identify(self, inspector):
        return inspector.onDocument(self)



# version
__id__ = "$Id$"

# End of file
