#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import wx
from .CommonInterface import CommonInterface


class Splitter(wx.SplitterWindow, CommonInterface):

    def __init__(self, parentWindow, minimumPanelSize = None):
        CommonInterface.__init__(self, parentWindow)
        
        wx.SplitterWindow.__init__(self, parentWindow)
        if minimumPanelSize: self.SetMinimumPaneSize( minimumPanelSize )
        return
    
        
    def add(self, window1, window2, orientation=None, sliderPosition = None):
        if orientation is None: orientation = "vertical"
        if sliderPosition is None: sliderPosition = 250
        if orientation == "horizontal":
            self.SplitHorizontally( window1, window2, sliderPosition )
            pass
        elif orientation == "vertical":
            self.SplitVertically( window1, window2, sliderPosition )
            pass
        else: raise ValueError("invalid splitting orientation: %s" % orientation)
        
        self.window1 = window1
        self.window2 = window2
        return        
    
    pass # end of Splitter



# version
__id__ = "$Id$"

# End of file 
