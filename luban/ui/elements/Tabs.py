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



from .TeleContainer import TeleContainer, Meta, TeleSection
from .ElementContainer import elementfactory


class Tabs(TeleContainer):


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
    tabs.tab('tab1').paragraph(text=['tab1 text'])
    tabs.tab('tab2').document(title='tab2')
        ''',
        ]

    abstract = False

    @elementfactory
    def tab(self, label=None, **kwds):
        tab = Tab(label=label, **kwds)
        self.append(tab)
        return tab


    def identify(self, inspector):
        return inspector.onTabs(self)





from .DocumentFactory import DocumentFactory
from .ParagraphFactory import ParagraphFactory
class Tab(DocumentFactory, ParagraphFactory, TeleSection, metaclass=Meta):


    simple_description = 'A tab in tabs'
    full_description = ''
    abstract = False

    label = descriptors.str(default='tab')
    label.tip = 'label of this tab'

    onselect = descriptors.action() # happen when this tab got selected
    onselect.tip = 'action when this tab is selected'

    def identify(self, inspector):
        return inspector.onTab(self)
    

# only allow tab(s) to be children of tabs
Tabs.allowed_element_types = [Tab]



class TabActions:

    def tab(self, actionname, **kwds):
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)



# version
__id__ = "$Id$"

# End of file
