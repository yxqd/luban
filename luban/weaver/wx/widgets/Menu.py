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


class Menu(wx.Menu, CommonInterface):

    def __init__(self, parent, text):
        CommonInterface.__init__(self, parent)
        wx.Menu.__init__(self)

        self.text = text
        self.items = {}
        return


    def append(self, menuitem):
        parentWindow = self

        id = menuitem.id
        text = menuitem.text
        help = menuitem.tip
        subMenu = menuitem.submenu 

        assert isinstance(text, basestring ),  ValueError(
            "%s(%s) is not a string" % (text, type(text)) )
        assert isinstance(help, basestring ),  ValueError(
            "%s(%s) is not a string" % (help, type(help)) )
        
        wxmenuitem =  wx.MenuItem(
            parentWindow,
            id = id,
            text = text,
            help = help,
            kind = wx.ITEM_NORMAL,
            subMenu = subMenu )
        
        callbacks = menuitem.callbacks
        from MenuItem import events
        #callback = callbacks.get('click')
        #if callback: 
        #    parent = self.parent
        #    wx.EVT_MENU(parent, id, callback)
        bindCallbacks(
            self.root, events, callbacks, source = None, id = id)
        
        self.AppendItem( wxmenuitem )
        self.items[ text ] = wxmenuitem
        return

    def appendMenu(self, menu):
        self.AppendMenu(-1, menu.text, menu)
        return

    def delete(self, menuitem):
        """ delete menuitem from this menu
        menuitem: text of the menu item that will be deleted
        """
        if menuitem not in self.items :
            raise "%s is not in this menu. menus are: %s" % (
                menuitem, self.items)
        wxmenuitem = self.items[ menuitem ]
        self.DeleteItem( wxmenuitem )
        del self.items[ menuitem ]
        return    

    def addChild(self, wxchild):
        try:
            self.append(wxchild)
        except:
            self.appendMenu(wxchild)
        return

    pass # end of Menu

# version
__id__ = "$Id$"

# End of file 
