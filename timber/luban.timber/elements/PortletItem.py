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


from luban.ui.elements.Riveted import RivetedContainer, Meta, RivetedSubElement

class PortletItem(RivetedContainer):


    # decorations
    simple_description = 'An item in a portlet'
    full_description = ''


    def identify(self, inspector):
        return inspector.onPortletItem(self)

    label = descriptors.str()
    label.tip = 'label of the portlet item'
    
    icon = descriptors.str()
    icon.tip = 'icon of the portlet item'
    
    tip = descriptors.str()
    tip.tip = 'tip for this portlet item that shows up when hovered'
    tip.experimental = True

    selected = descriptors.bool()
    selected.tip = 'if True, this item is selected'
    
    onselect = descriptors.action()
    onselect.tip = 'action when this portlet item is selected. usually this event handler is preferred over "onclick" event handler for this widget'


class PortletItemActions:

    def portlet(self, actionname, **kwds):
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)



# version
__id__ = "$Id$"

# End of file 
