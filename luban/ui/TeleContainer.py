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


from .ElementContainer import ElementContainer

class TeleContainer(ElementContainer):

    pass


from .ElementNotRoot import ElementNotRoot
class TeleSection(ElementContainer, ElementNotRoot):

    selected = ElementContainer.descriptors.bool(name='selected', default=False)
    
    pass


# version
__id__ = "$Id$"

# End of file 
