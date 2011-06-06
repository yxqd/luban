# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban.content.descriptors import *


# special descriptors for table
def radio_button(name, **kwds):
    return RadioButton(name, **kwds)


# select one row from a table. implemented as radio buttons
class RadioButton(Property):

    def __init__(self, name=None, default=None, meta=None):
        default = self._cast(default)
        Property.__init__(self, name, "radio_button", default, meta)
        return


    def _cast(self, value):
        return bool(value)



# version
__id__ = "$Id$"

# End of file 
