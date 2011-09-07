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


from .ActionBase import ActionBase as base, Meta

class NoAction(base):

    # decorations
    simple_description = 'nothing'
    full_description = ("no action at all")
    

    def identify(self, inspector):
        return inspector.onNoAction(self)

    
    def __repr__(self):
        return "NoAction()"
    

# version
__id__ = "$Id$"

# End of file 

