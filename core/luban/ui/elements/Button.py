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


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from .SimpleElement import SimpleElement as base
class Button(base):

    simple_description = 'A clickable button'
    full_description = (
        'A button is clickable. When clicked, an action will be triggered. '
        'A button has a label.'
        )
    

    # attributes
    label = descriptors.str()
    label.tip = 'label of the button'

    
    # for inspector
    def identify(self, inspector):
        return inspector.onButton(self)


# version
__id__ = "$Id$"

# End of file 
