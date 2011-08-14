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


"""
Frame: root of luban UI element hierarchy.
"""


from .SimpleContainer import SimpleContainer, Meta
class Frame(SimpleContainer, metaclass=Meta):
    
    simple_description = "root node of a luban user interface hierarchy"
    full_description = (
        'Frame element is the root element of a luban user interface.'
        'When a luban application starts up, an instance of Frame element'
        'needs to be established.'
        )

    abstract = False

    # means no element can be a frame's parent
    parent_types = None
    
    # attributes
    title = descriptors.str()
    title.tip = 'Title of the frame'
    
    # for inspector
    def identify(self, inspector):
        return inspector.onFrame(self)


# version
__id__ = "$Id$"

# End of file
