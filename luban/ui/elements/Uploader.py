#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                       (C) 2011  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from luban.content.Element import Element

class Uploader(Element):


    abstract = False
    

    def identify(self, visitor):
        return visitor.onUploader(self)

    label = descriptors.str(name='label')

    onsubmit = descriptors.eventHandler(name='onsubmit')
    oncomplete = descriptors.eventHandler(name='oncomplete')


# version
__id__ = "$Id$"

# End of file 
