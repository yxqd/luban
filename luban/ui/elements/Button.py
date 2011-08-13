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
class Button(base):

    simple_description = 'A clickable button'
    full_description = (
        'A button is clickable. When clicked, an action will be triggered. '
        'It can have a label and an icon.'
        )

    abstract = False

    # attributes
    label = descriptors.str()
    label.tip = 'label of the button'

    icon = descriptors.str()
    icon.tip = 'icon of the button'

    tip = descriptors.str()
    tip.tip = 'tip for the button that shows up when hovered'

    # for inspector
    def identify(self, inspector):
        return inspector.onButton(self)


# version
__id__ = "$Id$"

# End of file 
