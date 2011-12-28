# -*- Python -*-
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


from .Action import Action as base

class Alert(base):

    # decorations
    simple_description = 'an alert box with a message'
    full_description = ''

    
    # attributes
    message = descriptors.str()
    
    
    # methods
    def identify(self, inspector):
        return inspector.onAlert(self)


# version
__id__ = "$Id$"

# End of file 

