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


from .Element import Element


class FormField(Element):

    label = descriptors.str()
    help = descriptors.str()
    tip = descriptors.str()
    error = descriptors.str()
    value = descriptors.str()
    required = descriptors.bool()

    onchange = descriptors.action()
    onfocus = descriptors.action()
    onblur = descriptors.action()

# version
__id__ = "$Id$"

# End of file 
