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


class Portlet(base):

    # decorations
    simple_description = 'provides users access to dynamic content'
    full_description = (
        'A portlet usually is a small window. It contains items that, '
        'when clicked, lead to loading of dynamic content of UI. '
        'A portlet has a title which can be empty, and its children '
        'are of type PortletItem.'
        )
    
    # properties
    title = descriptors.str()
    title.tip = 'Title of the portlet'

    # methods
    def identify(self, inspector):
        return inspector.onPortlet(self)



class PortletItem(RivetedSubElement):
    
    # decorations
    simple_description = 'An item in a portlet'
    full_description = ''

    # properties
    label = descriptors.str()
    label.tip = 'label of the portlet item'
    
    icon = descriptors.str()
    icon.tip = 'icon of the portlet item'
    
    tip = descriptors.str()
    tip.tip = 'tip for this portlet item that shows up when hovered'
    tip.experimental = True

    selected = descriptors.bool()
    selected.tip = 'if True, this item is selected'
    
    # events
    from luban.ui.Event import Event
    class select(Event):
        # decorations
        simple_description = "event happens when this portlet is selected" 
        __unique_type_name__ = 'portletselect'
        # attributes
    del Event
    
    # methods
    def identify(self, inspector):
        return inspector.onPortletItem(self)



# version
__id__ = "$Id$"

# End of file 
