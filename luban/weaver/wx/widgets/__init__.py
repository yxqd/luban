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



def app(name):
    """app( name ) --> new app
    """
    from MainWinApp import MainWinApp
    return MainWinApp(name)


def mainFrame( **kwds ):
    "mainFrame(...) --> new main frame"
    from MainFrame import MainFrame
    return MainFrame( **kwds )


def matterbuilder(parentWindow, **kwds ):
    from science.MatterBuilder import MatterBuilder
    return MatterBuilder( parentWindow, **kwds )


def panel( parentWindow, **kwds ):
    from Panel import Panel
    return Panel( parentWindow, **kwds )


def htmlpanel( parentWindow, **kwds ):
    from HtmlPanel import HtmlPanel
    return HtmlPanel( parentWindow, **kwds )


def scienceCanvas(parentWindow, **kwds ):
    from science.Canvas import Canvas
    return Canvas( parentWindow, **kwds )


def splitter( parentWindow, **kwds):
    from Splitter import Splitter
    return Splitter( parentWindow, **kwds)


def notebook( parentWindow, **kwds):
    from Notebook import Notebook
    return Notebook( parentWindow, **kwds)


def text( parentWindow, txt, **kwds):
    from StaticText import StaticText
    text = StaticText( parentWindow, txt, **kwds )
    return text


def sizer( **kwds ):
    from Sizer import Sizer
    return Sizer( **kwds )


def listbox(parentWindow, **kwds):
    from ListBox import ListBox
    return ListBox( parentWindow, **kwds )


def matterBuilder(parentWindow):
    from  science.MatterBuilder import MatterBuilder
    return MatterBuilder(parentWindow)


def menu(parentWindow, text):
    from  Menu import Menu
    return Menu(parentWindow, text)


def menubar(*args, **kwds):
    from MenuBar import MenuBar
    return MenuBar(*args, **kwds)


def menuitem(parent, **kwds):
    from MenuItem import MenuItem
    return MenuItem( parent, **kwds)


def progressbar(parent, **kwds):
    from ProgressBar import ProgressBar
    return ProgressBar( parent, **kwds)


def loadfileDialog(parentWindow, title, defaultDir = '.'):
    import wx
    d = wx.FileDialog( parentWindow, title, defaultDir = defaultDir)
    if d.ShowModal() != wx.ID_OK: d.Destroy(); return
    file = d.GetPath()
    d.Destroy()
    return file


def textentryDialog( parentWindow, caption, message, default = "Input your text" ):
    import wx
    d = wx.TextEntryDialog(
        parentWindow, message=message, caption=caption, defaultValue = default)
    if d.ShowModal() != wx.ID_OK: d.Destroy(); return
    value = d.GetValue()
    d.Destroy()
    return value


def dirDialog( parentWindow, title, defaultDir = "." ):
    import wx
    d = wx.DirDialog( parentWindow, title, defaultDir)
    if d.ShowModal() != wx.ID_OK: d.Destroy(); return
    path = d.GetPath()
    d.Destroy()
    return path


def messageDialog(parentWindow, title, message):
    import wx
    d= wx.MessageDialog( parentWindow, message, title, wx.OK)
    d.ShowModal() # Shows it
    d.Destroy() # finally destroy it when finished.
    return


def savefileDialog(parentWindow, title, filetypes):
    import wx
    dlg =wx.FileDialog(parentWindow, message = title,
                       defaultDir = "", defaultFile = "",
                       wildcard = filetypes,
                       style = wx.SAVE|wx.OVERWRITE_PROMPT|wx.CHANGE_DIR)
    rt = None
    if dlg.ShowModal() == wx.ID_OK:
        dirname  = dlg.GetDirectory()
        filename = dlg.GetFilename()
        import os
        rt = os.path.join(dirname, filename)
        pass
    dlg.Destroy()
    return rt


def dialog(parentWindow, **kwds ):
    from Dialog import Dialog
    return Dialog( parentWindow, **kwds )


def button(parentWindow, **kwds ):
    from Button import Button
    return Button( parentWindow, **kwds )


def buttonWithIcon(parentWindow, **kwds ):
    from ButtonWithIcon import ButtonWithIcon
    return ButtonWithIcon( parentWindow, **kwds )


def form(parentWindow, **kwds):
    from Form import Form
    return Form(parentWindow, **kwds)


def formfield(parentWindow, **kwds):
    from FormField import FormField
    return FormField(parentWindow, **kwds)


def textfield(parentWindow, **kwds ):
    from TextField import TextField
    return TextField( parentWindow, **kwds )


def passwordfield(parentWindow, **kwds ):
    from PasswordField import PasswordField
    return PasswordField( parentWindow, **kwds )


def treeviewContainer(parentWindow, **kwds ):
    from TreeViewContainer import TreeViewContainer
    return TreeViewContainer (parentWindow, **kwds )


def treeview(parentWindow, **kwds ):
    from TreeView import TreeView
    return TreeView (parentWindow, **kwds )


def choice(parent, **kwds):
    from Choice import Choice
    return Choice(parent, **kwds)


def link(parent, **kwds):
    from Link import Link
    return Link(parent, **kwds)


def accordion(parent, **kwds):
    from Accordion import Accordion
    return Accordion(parent, **kwds)


def radiobox(parent, **kwds):
    from RadioBox import RadioBox
    return RadioBox(parent, **kwds)


def checkbox(parent, **kwds):
    from CheckBox import CheckBox
    return CheckBox(parent, **kwds)


def histogramPlotter(parent, **kwds):
    from HistogramPlotPanel import HistogramPlotPanel
    return HistogramPlotPanel(parent, **kwds)


def table(parent, **kwds):
    from Table import Table
    return Table(parent, **kwds)


# version
__id__ = "$Id$"

# End of file 
