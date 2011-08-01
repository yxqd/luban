#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin     
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .DocumentFactory import DocumentFactory
from .SimpleContainer import SimpleContainer, Meta


class Frame(DocumentFactory, SimpleContainer, metaclass=Meta):

    simple_description = "root node of a luban user interface hierarchy"
    full_description = (
        'Frame element is the root element of a luban user interface.'
        'When a luban application starts up, an instance of Frame element'
        'needs to be established.'
        )

    abstract = False


    def identify(self, inspector):
        return inspector.onFrame(self)


    title = descriptors.str()
    title.tip = 'Title of the frame'
    

# version
__id__ = "$Id$"

# End of file
