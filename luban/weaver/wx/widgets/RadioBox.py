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


class RadioBox(wx.RadioBox, CommonInterface):

    def __init__(self, parentWindow, choices=[], name=''):
        CommonInterface.__init__(self, parentWindow)
        wx.RadioBox.__init__(self, parentWindow, choices=choices, name=name,
                             style=wx.RA_VERTICAL)
        return

    def value(self):
        return self.GetSelection()
    

    pass # end of RadioBox

# version
__id__ = "$Id$"

# End of file 
