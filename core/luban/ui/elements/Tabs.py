#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                   Jiao Lin
#                        California Institute of Technology
#                        (C) 2006-2011  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from .Riveted import RivetedContainer, Meta, RivetedSubElement
from .ElementContainer import elementfactory


class Tabs(RivetedContainer):


    # decorations
    simple_description = 'A container of tabs'
    full_description = (
        "A 'tabs' element is a container of 'tab' elements. "
        "The widget shows one tab at a time. Usually, when a tab "
        "is clicked, it shows up. "
        )
    examples = [
        '''
from luban.ui import e as lue
tabs = lue.tabs()
tabs.tab('tab1').paragraph(text='tab1 text')
tabs.tab('tab2').document(title='tab2')
''',
        ]
    

    # methods
    # .. for inspector
    def identify(self, inspector):
        return inspector.onTabs(self)




from .SimpleContainer import SimpleContainer
class Tab(RivetedSubElement, SimpleContainer, metaclass=Meta):

    
    # decorations
    simple_description = 'A tab in a "tabs" container'
    full_description = ''
    
    #
    parent_types = [Tabs]

    # attributes
    label = descriptors.str(default='tab')
    label.tip = 'label of this tab'

    selected = descriptors.bool()
    selected.tip = "whether this tab is selected or not. among siblings, only one can be selected"

    # events -- must have one-one correspondence with event handler
    from ..Event import Event
    class select(Event):
        # decorations
        simple_description = "event happens when this tab is selected"        
        __unique_type_name__ = 'tabselect'
        # attributes
        oldtab = descriptors.str()
        newtab = descriptors.str()
    del Event

    # ************************************************************
    # event handlers
    # event handlers will be automatically defined using event types
    # defined here (like "select" event above will cause a "onselect"
    # event handler automatically)
    # here is just an example in case one has to define a custom 
    # event handler descriptor
    # onselect = descriptors.eventhandler() # happen when this tab got selected
    # onselect.tip = 'action when this tab is selected'
    # ************************************************************

    # for inspector
    def identify(self, inspector):
        return inspector.onTab(self)
    

Tabs.child_types = [Tab]


def tab(self, label=None, **kwds):
    from .SubElementFactory import createSubElement
    return createSubElement(self, Tab, label=label, **kwds)
tab.__doc__ = Tab.getCtorDocStr(ctor_name = 'tab')
Tabs.tab = elementfactory(tab)


# to define a new element action, subclass ElementActionBase
from ..actions.ElementActionBase import ElementActionBase
class TabSelectAction(ElementActionBase):

    "select the tab"

    # decorations
    element_type = Tab
    factory_method = "select"


    # methods
    def identify(self, visitor):
        return visitor.onTabSelectAction(self)




# End of file
