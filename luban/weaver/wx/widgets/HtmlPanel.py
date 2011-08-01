#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                      California Institute of Technology
#                       (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import wx
import wx.html as html
from .CommonInterface import CommonInterface



class HtmlPanel(html.HtmlWindow, CommonInterface):
    
    
    def __init__(self, parentWindow, borderStyle=None, name=''):

        CommonInterface.__init__(self, parentWindow)
        
        from .globalID import create
        self.id = create()
        
        html.HtmlWindow.__init__(self, parentWindow, self.id, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        
        return
    
    
#    def setContent(self, text):
#        pass



# version
__id__ = "$Id$"

# End of file 
