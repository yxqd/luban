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
from .CommonInterface import CommonInterface


class Choice(wx.Choice, CommonInterface):

    def __init__(self, parent, choices = [], pos = None, size = (200,-1),
                 name = "", id = -1, style=0):
        
        CommonInterface.__init__(self, parent)
        
        wx.Choice.__init__(
            self, parent, id = id, 
            pos = pos, size = size,
            choices = choices,
            style = style,
            name = name)
        
        return


    def value(self):
        return self.GetCurrentSelection()

    pass # end of TextField

# version
__id__ = "$Id$"

# End of file 
