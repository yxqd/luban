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


class FormField(wx.Panel, CommonInterface):
    
    
    def __init__(self, parent, name = "", **kwds):
        CommonInterface.__init__(self, parent)
        wx.Panel.__init__(self, parent, id = -1, name=name, **kwds)
        return
    
    
    def showerrormessage(self, message):
        warnings.warn("formfield.showerrormessage(...) is obsolete, please use formfield.showError(...)", DeprecationWarning)
        return self.showError(message)
    
    
    def showError(self, message):
        caption = 'Error'
        wx.MessageBox(message, caption, wx.OK)
        return
    
    
    pass # end of TextField

import warnings

# version
__id__ = "$Id$"

# End of file 
