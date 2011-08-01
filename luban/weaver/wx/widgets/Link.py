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
from .ext import bindCallbacks

events = {
    'click': wx.EVT_HYPERLINK,
    }

class Link(wx.HyperlinkCtrl, CommonInterface):
    

    def __init__(self, parent, callbacks={}, label=None):
        
        CommonInterface.__init__(self, parent)

        from .globalID import create
        id = create()

        wx.HyperlinkCtrl.__init__(self, parent, id, label, '')

        # binds callbacks. 
        if callbacks:
            bindCallbacks(parent, events, callbacks, id=id)

        return

    pass # end of Link

# version
__id__ = "$Id$"

# End of file 
