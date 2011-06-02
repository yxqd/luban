#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                       (C) 2009  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from luban.content.Element import Element

class Uploader(Element):


    abstract = False
    

    def identify(self, visitor):
        return visitor.onUploader(self)

    label = Element.descriptors.str(name='label')

    onsubmit = Element.descriptors.eventHandler(name='onsubmit')
    oncomplete = Element.descriptors.eventHandler(name='oncomplete')


# version
__id__ = "$Id$"

# End of file 
