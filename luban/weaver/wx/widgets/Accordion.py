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
import wx.lib.agw.foldpanelbar as fpb
from ext import bindCallbacks

events={'click': fpb.EVT_CAPTIONBAR}

from CommonInterface import CommonInterface

class Accordion(fpb.FoldPanelBar, CommonInterface):

    def __init__(self, parent):#, callbacks={}):
        
        CommonInterface.__init__(self, parent)
        
        fpb.FoldPanelBar.__init__(self, parent, wx.ID_ANY, 
                     wx.DefaultPosition, wx.DefaultSize, fpb.FPB_DEFAULT_STYLE,
                     fpb.FPB_SINGLE_FOLD) 

        #if callbacks:
        #    bindCallbacks(parent, events, callbacks)

        self.contents = []
        self.clicks = []
        
        return

    
    def bindcallbacks(self, callbacks):
        bindCallbacks(self, events, callbacks)

        
    def append(self, window, foldpanel):
        self.AddFoldPanelWindow(foldpanel, window)
        self.AddFoldPanelSeparator(foldpanel)
        self.contents.append(foldpanel)
        return

    
    def addChild(self, child):
        self.append(child[1], child[0])

        
    pass # end of Accordion

# version
__id__ = "$Id$"

# End of file 
