# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from PropertyInterface import PropertyInterface

from pyre.inventory.Property import Property

class Date(PropertyInterface, Property):

    def __init__(self, name, **kwds):
        Property.__init__(self, name, type='date', **kwds)
        return



# version
__id__ = "$Id$"

# End of file 
