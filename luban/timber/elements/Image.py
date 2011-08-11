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


from .SimpleElement import SimpleElement as base


class Image(base):

    simple_description = 'An image'
    full_description = (
        'An image widget displays an image'
        )

    abstract = False

    path = descriptors.str()
    path.tip = 'path to the image'
    

    def identify(self, inspector):
        return inspector.onImage(self)


# version
__id__ = "$Id$"

# End of file 
