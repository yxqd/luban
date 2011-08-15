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



from .RivetedContainer import RivetedContainer, Meta, RivetedSubElement
from .ElementContainer import elementfactory


class Tabs(RivetedContainer):


    simple_description = 'A container of tabs'
    full_description = (
        "A 'tabs' element is a container of 'tab' elements. "
        "The widget shows one tab at a time. Usually, when a tab "
        "is clicked, it shows up. "
        )
    examples = [
        '''
import luban.ui.elements
tabs = luban.ui.elements.tabs()
tabs.tab('tab1').paragraph(text='tab1 text')
tabs.tab('tab2').document(title='tab2')
''',
        ]
    
    abstract = False

    
    @elementfactory
    def tab(self, label=None, **kwds):
        from .SubElementFactory import createSubElement
        return createSubElement(self, Tab, label=label, **kwds)


    def identify(self, inspector):
        return inspector.onTabs(self)




from .SimpleContainer import SimpleContainer
class Tab(RivetedSubElement, SimpleContainer, metaclass=Meta):


    simple_description = 'A tab in tabs'
    full_description = ''
    abstract = False

    #
    parent_types = [Tabs]

    # attributes
    label = descriptors.str(default='tab')
    label.tip = 'label of this tab'

    onselect = descriptors.eventhandler() # happen when this tab got selected
    onselect.tip = 'action when this tab is selected'

    # for inspectorx
    def identify(self, inspector):
        return inspector.onTab(self)
    


# End of file
