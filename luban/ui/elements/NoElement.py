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


from .ElementBase import ElementBase as base, Meta

class NoElement(base):

    simple_description = 'nothing'
    full_description = ("no element at all")

    abstract = False

    def identify(self, inspector):
        return inspector.onNoElement(self)
    

# version
__id__ = "$Id$"

# End of file 

