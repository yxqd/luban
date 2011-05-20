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


from Panel import borderStyles


#from wx import Notebook as base
import wx.lib.agw.flatnotebook as fnb
base = fnb.FlatNotebook
class Notebook(base, CommonInterface):

    def __init__(self, parentWindow, borderStyle = None, size=None):

        CommonInterface.__init__(self, parentWindow)
        
        if borderStyle is None:
            borderStyle = 'default'
        style = borderStyles[ borderStyle ]
        base.__init__(self, parentWindow, style=style, size=size)

        self.pages = []
        self.labels = []
        return
    
        
    def add(self, title, page):
        self.AddPage( page, title )
        self.pages.append( page )
        self.labels.append(title)
        return    


    def DoGetBestSize(self):
        """ Overrides DoGetBestSize to handle sizers nicely. """

        if not self._windows:
            # Something is better than nothing... no pages!
            return wx.Size(20, 20)

        maxWidth = maxHeight = 0
        
        # deal with the case where each page is small
        # so that the size of the notebook is too small and the
        # titles of notebook are not displayed where
        # here we set maxWidth to about the width of longest title
        maxWidth = max(map(len, self.labels)) * 20
        
        tabHeight = self.GetPageBestSize().height

        for win in self._windows:
            # Loop over all the windows to get their best size
            width, height = win.GetBestSize()
            maxWidth, maxHeight = max(maxWidth, width), max(maxHeight, height)

        return wx.Size(maxWidth, maxHeight+tabHeight)


    pass # end of Notebook



# version
__id__ = "$Id$"

# End of file 

