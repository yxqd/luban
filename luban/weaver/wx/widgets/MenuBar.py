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


class MenuBar(wx.MenuBar, CommonInterface):
    

    def __init__(self, parent=None):
        CommonInterface.__init__(self, parent)
        wx.MenuBar.__init__(self)
        return


    def append(self, menu):
        self.Append( menu, menu.text )
        return
    

    pass # end of MenuBar

# version
__id__ = "$Id$"

# End of file 
