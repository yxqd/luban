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


from Element import Element


class FormField(Element):

    label = Element.descriptors.str(name='label')
    help = Element.descriptors.str(name='help')
    tip = Element.descriptors.str(name='tip')
    error = Element.descriptors.str(name='error')
    value = Element.descriptors.str(name='value')
    required = Element.descriptors.bool(name='required')

    onchange = Element.descriptors.eventHandler(name='onchange')
    onfocus = Element.descriptors.eventHandler(name='onfocus')
    onblur = Element.descriptors.eventHandler(name='onblur')

# version
__id__ = "$Id$"

# End of file 
