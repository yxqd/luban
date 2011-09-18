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
from luban.ui.elements.ElementContainer import elementfactory


class Portlet(RivetedContainer):

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
    @elementfactory
    def item(self, **kwds):
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, PortletItem, **kwds)
    
    
    def identify(self, inspector):
        return inspector.onPortlet(self)


from luban.ui.elements.SimpleElement import SimpleElement
class PortletItem(RivetedSubElement, SimpleElement, metaclass=Meta):
    
    # decorations
    simple_description = 'An item in a portlet'
    full_description = ''

    #
    parent_types = [Portlet]

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


Portlet.child_types = [PortletItem]


# actions
# to define a new element action, subclass ElementActionBase
from luban.ui.actions.ElementActionBase import ElementActionBase
class SelectPortletItem(ElementActionBase):

    "select a portlet item"

    # decorations
    element_type = PortletItem
    factory_method = "select"


# End of file 
