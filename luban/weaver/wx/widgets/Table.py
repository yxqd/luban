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
import wx.grid

from CommonInterface import CommonInterface

class Table(wx.grid.Grid, CommonInterface):

    def __init__(self, parent, model, view, data):
        # call my ancestors ctors
        CommonInterface.__init__(self, parent)
        wx.grid.Grid.__init__(self, parent)

        # 
        #self.changedcells = []
        #self.columns = []

        # reference to data
        self.data = data

        # measures
        measures = {}
        for descriptor in model.iterDescriptors():
            measures[descriptor.name] = descriptor
            continue

        # columns
        allcolumns = view.columns
        visiblecols = filter(lambda col: not col.hidden, allcolumns)
        self.colnames = [col.measure for col in visiblecols]

        # links are special
        linkcols = filter(lambda col: measures[col.measure].type == 'link', allcolumns)
        self.linkcolindexes = [visiblecols.index(col) for col in linkcols]

        # if there are links, we need to create a special renderer
        if self.linkcolindexes:
            self.linkcellrenderer = LinkCellRenderer()
        self.colrenderers = [None for i in self.colnames]
        for index in self.linkcolindexes:
            self.colrenderers[index] = self.linkcellrenderer

        # size
        height = len(data)
        width = len(visiblecols)
        self.CreateGrid(height, width)

        # pass 'measure' attributes to the wxtable
        #for column in allcolumns:
        #    self.columns.append(column.measure)

        # editable defaults to False
        if not view.editable:
            for x in range(height):
                for y in range(width):
                    self.SetReadOnly(x, y)

        # set column labels
        for n, c in enumerate(visiblecols):
            self.SetColLabelValue(n, c.label)
            if not c.editable:
                for x in range(height):
                    self.SetReadOnly(x, n)

        # populate the table with data
        for x, d in enumerate(data):
            for y, value in enumerate(d):

                value = _celltext(value)

                self.SetCellValue(x, y, value)

                renderer = self.colrenderers[y]
                if renderer:
                    self.SetCellRenderer(x, y, renderer)

        self.AutoSize()

        # turn off row labels
        self.SetRowLabelSize(0)

        #
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.onMouse)
        return


    def getColName(self, colno):
        return self.colnames[colno]


    def getCellValue(self, row, colname):
        col = self.colnames.index(colname)
        return self.GetCellValue(row, col)


    def onMouse(self, evt):
        if evt.Col in self.linkcolindexes:
            link = self.data[evt.Row][evt.Col]
            onclick = link.onclick_compiled
            onclick(evt=None)
            evt.Skip(False)
            return
        
        evt.Skip()
        return
    

    pass # end of Table


import operator
_celltext_handlers = {
    'default': str,
    'link': operator.attrgetter('label'),
    }
def _celltext(value):
    typename = value.__class__.__name__.lower()
    if typename not in _celltext_handlers:
        typename = 'default'
    handler = _celltext_handlers[typename]
    return handler(value)


gridlib = wx.grid
class LinkCellRenderer(gridlib.PyGridCellRenderer):

    
    def __init__(self):
        gridlib.PyGridCellRenderer.__init__(self)
        

    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        dc.SetBackgroundMode(wx.SOLID)
        dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangleRect(rect)

        dc.SetBackgroundMode(wx.TRANSPARENT)
        dc.SetFont(attr.GetFont())

        text = grid.GetCellValue(row, col)
        color = 'SKY BLUE'
        x = rect.x + 1
        y = rect.y + 1

        dc.SetTextForeground(color)
        dc.DrawText(text, x, y)
        #w, h = dc.GetTextExtent(ch)
        return


    def GetBestSize(self, grid, attr, dc, row, col):
        text = grid.GetCellValue(row, col)
        dc.SetFont(attr.GetFont())
        w, h = dc.GetTextExtent(text)
        return wx.Size(w, h)


    def Clone(self):
        return LinkCellRenderer()

# version
__id__ = "$Id$"

# End of file 
