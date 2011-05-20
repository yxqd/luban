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
from CommonInterface import CommonInterface


class MainFrame(wx.Frame, CommonInterface):
    
    def __init__(self, parent=None, title='Title', #size = (1000, 700),
                 position = wx.DefaultPosition):

        self.root = self
        wx.Frame.__init__(self, parent, -1, title, position)#, size)

        CommonInterface.__init__(self, parent or self)
        
        self.draw()
        return

    def draw(self):
        self.CreateStatusBar()
        return


    def setAttribute(self, **attrs):
        if 'title' in attrs:
            title = attrs['title']
            self.SetTitle(title)

    pass # end of MainFrame



# version
__id__ = "$Id$"

# End of file 
