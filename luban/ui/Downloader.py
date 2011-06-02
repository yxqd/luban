#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                     (C) 2011-2010  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from luban.content.Element import Element

class Downloader(Element):


    simple_description = 'A widget when clicked download a file from controller'
    full_description = (
        'A downloader is a link/button like widget that when clicked, '
        'retrieves a resource from the controller and prompts user '
        'to save it.'
        )

    abstract = False
    

    def identify(self, visitor):
        return visitor.onDownloader(self)
    
    label = Element.descriptors.str(name='label')
    label.tip = 'label for the downloader'
    
    ondownload = Element.descriptors.eventHandler(name='ondownload')
    ondownload.tip = (
        'The loading action that loads the resource from the controller. '
        'The ondownload property must be assigned a loading action, '
        'which can be constructed using factory luban.content.load. '
        'On the controller side, the routine that reponds to this '
        'loading request must returns a resource, such as an instace '
        'of luban.content.File.File.'
        )

# version
__id__ = "$Id$"

# End of file 
