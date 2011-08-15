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


"""NoElement: null element

TOTHINK: is None good enough?
"""


from .ElementBase import ElementBase as base, Meta

class NoElement(base):

    """special type of null element
    """

    simple_description = 'nothing'
    full_description = ("no element at all")

    abstract = False

    def identify(self, inspector):
        return inspector.onNoElement(self)
    

# version
__id__ = "$Id$"

# End of file 

