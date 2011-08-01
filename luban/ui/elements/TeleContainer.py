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


from .ElementContainer import ElementContainer, Meta

class TeleContainer(ElementContainer):

    pass


from .ElementNotRoot import ElementNotRoot
class TeleSection(ElementNotRoot, ElementContainer, metaclass=Meta):

    selected = descriptors.bool()
    
    pass


# version
__id__ = "$Id$"

# End of file 
