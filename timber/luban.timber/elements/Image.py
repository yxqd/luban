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


from luban.ui.elements.SimpleElement import SimpleElement as base
class Image(base):

    # decorations
    simple_description = 'An image'
    full_description = (
        'An image widget displays an image'
        )

    # properties
    path = descriptors.str()
    path.tip = 'path to the image'
    
    # methods
    def identify(self, inspector):
        return inspector.onImage(self)


# End of file 
