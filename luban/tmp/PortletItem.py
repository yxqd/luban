#!/usr/bin/env python
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


from .ElementContainer import ElementContainer

class PortletItem(ElementContainer):


    abstract = False
    simple_description = 'An item in a portlet'
    full_description = ''


    def identify(self, inspector):
        return inspector.onPortletItem(self)

    label = ElementContainer.descriptors.str(name='label')
    label.tip = 'label of the portlet item'
    
    icon = ElementContainer.descriptors.str(name='icon')
    icon.tip = 'icon of the portlet item'
    
    tip = ElementContainer.descriptors.str(name='tip')
    tip.tip = 'tip for this portlet item that shows up when hovered'
    tip.experimental = True

    selected = ElementContainer.descriptors.bool(name='selected', default=False)
    selected.tip = 'if True, this item is selected'
    
    onselect = ElementContainer.descriptors.eventHandler(name='onselect')
    onselect.tip = 'event handler that triggers when this portlet item is selected. usually this event handler is preferred over "onclick" event handler for this widget'


class PortletItemActions:

    def portlet(self, actionname, **kwds):
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)



# version
__id__ = "$Id$"

# End of file 
