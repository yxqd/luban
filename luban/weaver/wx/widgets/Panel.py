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


borderStyles = {
    "sunken": wx.BORDER_SUNKEN,
    'default': wx.BORDER_DEFAULT,
    }



class Panel(wx.Panel, CommonInterface):
    
    
    def __init__(self, parentWindow, borderStyle=None, name=''):

        CommonInterface.__init__(self, parentWindow)

        if borderStyle is None:
            borderStyle = 'default'
        style = borderStyles[ borderStyle ]
        wx.Panel.__init__(self, parentWindow, style = style, name=name)
        
        return


    def setAttribute(self, **kwds):
        if 'title' in kwds:
            title = kwds['title']
            self.titlewidget.SetLabel(title)
        return
    
    
    pass # end of Panel



# version
__id__ = "$Id$"

# End of file 
