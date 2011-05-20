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
from ext import bindCallbacks

events = {}

class ProgressBar(wx.Panel, CommonInterface):

    def __init__(self, parent, checking=None, finished=None, skip=300):
        
        CommonInterface.__init__(self, parent)

        wx.Panel.__init__(self, parent)

        self.checking = checking
        self.finished = finished
        self.skip = skip
        
        return

    def startTimer(self):
        self.timer = wx.Timer(self)

        self.timer.Start(self.skip)

        def onTimer(evt):
            self.checking(evt)
            if self.gauge.GetValue() >= 100:
                self.timer.Stop()
                self.finished(evt)

        self.Bind(wx.EVT_TIMER, onTimer, self.timer)
        return

    def setAttribute(self, **attrs):
        if 'percentage' in attrs:
            percentage = attrs['percentage']
            self.gauge.SetValue(percentage)

        if 'status' in attrs:
            status = attrs['status']
            self.status.SetLabel(status)

    pass # end of ProgressBar

# version
__id__ = "$Id$"

# End of file 
