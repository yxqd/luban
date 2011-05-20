#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import wx

from TextField import TextField

class PasswordField(TextField):

    def __init__(self, parent, **kwds):
        super(PasswordField, self).__init__(
            parent, style=wx.TE_PASSWORD, **kwds)
        return

    pass # end of TextField


# version
__id__ = "$Id$"

# End of file 
