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
from CommonInterface import CommonInterface


class CheckBox(wx.CheckBox, CommonInterface):

    def __init__(self, parent, value = False, pos = None, size = None,
                 name = "", **kwds):
        CommonInterface.__init__(self, parent)
        wx.CheckBox.__init__(self, parent, id = -1, 
                             pos = pos, size = size, name = name, **kwds)
        self.SetValue(value)
        return


    def value(self):
        return self.GetValue()

    pass # end of TextField

# version
__id__ = "$Id$"

# End of file 
