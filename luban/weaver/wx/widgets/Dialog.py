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


styles = {
    'default': wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
    }


class Dialog(wx.Dialog, CommonInterface):
    
    def __init__(self, parentWindow,
                 title = "title",
                 size = (600,500),
                 pos = wx.DefaultPosition,
                 style = 'default'
                 ):

        CommonInterface.__init__(self, parentWindow)
        
        style = styles[ style ]

        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        
        pre.Create(parentWindow, -1, title, pos, size, style)
        self.PostCreate(pre)
        return


    def show(self):
        self.ret = self.ShowModal()
        return
    open = show


    def ok(self):
        return self.ret == wx.ID_OK


    def destroy(self):
        self.Destroy()
        return
    close = destroy
    
    pass # end of Dialog



# version
__id__ = "$Id$"

# End of file 
