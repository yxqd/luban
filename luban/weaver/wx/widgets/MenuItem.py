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
from CommonInterface import CommonInterface


events = {
    'click': wx.EVT_MENU,
    }


class MenuItem(CommonInterface):
    
    
    def __init__(self, parent=None, text="menutext", tip="helptext",
                 callbacks={}, submenu = None):
        
        CommonInterface.__init__(self, parent)
        
        from globalID import create
        id = create()
        
        self.id = id
        self.text = text
        self.tip = tip
        self.submenu = submenu
        self.callbacks = callbacks
        
        return

    pass # end of MenuItem


# version
__id__ = "$Id$"

# End of file 
