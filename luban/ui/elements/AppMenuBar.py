# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .Element import Element
from .ElementContainer import ElementContainer, elementfactory



class AppMenuItem(Element):

    simple_description = 'A menu item in a menu in the application menu bar'
    full_description = ''
    abstract = False
    experimental = True

    label = descriptors.str()
    label.tip = 'label of the menu item'
    
    icon = descriptors.str()
    icon.tip = 'icon of the menu item'
    icon.experimental = True
    
    tip = descriptors.str()
    tip.tip = 'tip for the menu item that shows up when hovered'
    tip.experimental = True

    def identify(self, visitor):
        return visitor.onAppMenuItem( self )



class AppMenu(ElementContainer):

    simple_description = 'a menu in the application menu bar or a submenu in a menu in the application menu bar'
    full_description = ''
    abstract = False


    label = descriptors.str()
    label.tip = 'label of the menu'
    
    icon = descriptors.str()
    icon.tip = 'icon of the menu'
    icon.experimental = True
    
    tip = descriptors.str()
    tip.tip = 'tip for the menu that shows up when hovered'
    tip.experimental = True

    @elementfactory
    def menu(self, *args, **kwds):
        b = AppMenu(*args, **kwds)
        self.add(b)
        return b

    @elementfactory
    def item(self, *args, **kwds):
        l = AppMenuItem(*args, **kwds)
        self.add(l)
        return l


    def identify(self, renderer):
        return renderer.onAppMenu(self)
        


class AppMenuBar(ElementContainer):

    simple_description = 'Application menu bar'
    full_description = ''
    
    abstract = False

    @elementfactory
    def menu(self, *args, **kwds):
        b = AppMenu(*args, **kwds)
        self.add(b)
        return b

    @elementfactory
    def item(self, *args, **kwds):
        l = AppMenuItem(*args, **kwds)
        self.add(l)
        return l


    def identify(self, visitor):
        return visitor.onAppMenuBar(self)


# only allow appmenu to be children of appmenubar
AppMenuBar.allowed_element_types = [AppMenu, AppMenuItem]

# only allow appmenuitem to be children of appmenu
AppMenu.allowed_element_types = [AppMenu, AppMenuItem]


# version
__id__ = "$Id$"

# End of file 
