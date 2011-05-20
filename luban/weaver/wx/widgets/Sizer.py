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


orientations = {
    "horizontal": wx.HORIZONTAL,
    "vertical": wx.VERTICAL,
    }
    

default_flag = wx.ALL
#default_flag = wx.ALIGN_LEFT
#default_flag = wx.GROW|wx.ALL

class Sizer(wx.BoxSizer):

    def __init__(self, orientation = "horizontal"):
        orientation = orientations[orientation]
        wx.BoxSizer.__init__(self, orientation)
        self.added = []
        return
    

    def add(self, element, proportion=0, border=2, flag=default_flag):
        self.added.append(element)
        return wx.Sizer.Add(self, element, proportion, flag, border)


    def wasAlreadyAdded(self, element):
        return element in self.added
    

    pass # end of Sizer

# version
__id__ = "$Id$"

# End of file 
