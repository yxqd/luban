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

    label = descriptors.str(name='label')
    help = descriptors.str(name='help')
    tip = descriptors.str(name='tip')
    error = descriptors.str(name='error')
    value = descriptors.str(name='value')
    required = descriptors.bool(name='required')

    onchange = descriptors.eventHandler(name='onchange')
    onfocus = descriptors.eventHandler(name='onfocus')
    onblur = descriptors.eventHandler(name='onblur')

# version
__id__ = "$Id$"

# End of file 
