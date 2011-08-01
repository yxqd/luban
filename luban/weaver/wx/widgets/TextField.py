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
from .CommonInterface import CommonInterface


class TextField(wx.TextCtrl, CommonInterface):

    def __init__(self, parent, value = '', pos = None, size = (200,-1),
                 name = "", **kwds):
        CommonInterface.__init__(self, parent)
        wx.TextCtrl.__init__(self, parent, id = -1, value = value,
                             pos = pos, size = size, name = name, **kwds)
        return


    def value(self):
        return self.GetValue()

    pass # end of TextField

# version
__id__ = "$Id$"

# End of file 
