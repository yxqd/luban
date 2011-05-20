#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import wx
from CommonInterface import CommonInterface


class StaticText(wx.StaticText, CommonInterface):

    def __init__(self, parent, text, id=-1, **kwds):
        CommonInterface.__init__(self, parent)
        wx.StaticText.__init__(self, parent, id, text, **kwds )
        return

    pass # end of TextField


# version
__id__ = "$Id$"

# End of file 
