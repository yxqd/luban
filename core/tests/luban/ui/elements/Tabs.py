#!/usr/bin/env python3
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import luban


import unittest
class TestCase(unittest.TestCase):

    def test0(self):
        examples = luban.e.tabs().examples
        code = '\n'.join(examples)
        exec(code)
        return
    
     
    def test1(self):
        tabs = luban.e.tabs()
        tabs.tab().document(title='doc1').paragraph(text='hello')
        tabs.tab().tabs()
        # print(tabs)
        return


    def test2(self):
        tabs = luban.e.tabs()
        self.assertRaises(AttributeError, getattr, tabs, 'document')
        return


    def test3(self):
        tabs = luban.e.tabs()
        tab1 = tabs.tab(id='tab1')
        selecttab1 = luban.a.select(element=tab1).select()
        print(selecttab1)
        return


    def test4(self):
        tabs = luban.e.tabs()
        tab1 = tabs.tab(id='tab1')
        from luban.ui.descriptors.Descriptor import Descriptor
        self.assert_(isinstance(tab1.__class__.onselect, Descriptor))
        tab1.onselect = luban.a.alert("hello")
        from luban.ui.actions.Action import Action
        self.assert_(isinstance(tab1.onselect, Action))
        return


    def test5(self):
        tabs = luban.e.tabs()
        tab1 = tabs.tab(id='tab1')
        from luban.ui.descriptors.EventHandler import EventAttributeError
        try:
            tab1.onselect = luban.a.load(actor="actor", param1=luban.event.x)
        except EventAttributeError:
            pass
        else:
            raise RuntimeError("should raise EventAttributeError")
        return

    
    def test6(self):
        """luban.content.ElementContainer: allowed_element_types: Tabs"""
        from luban.ui.elements.Tabs import Tabs, Tab
        tabs = Tabs()
        tabs.tab(name='tab1')

        tabs.append(Tab(name="tab2"))

        from luban.ui.elements.Document import Document
        self.assertRaises(
            tabs.SubelementDisallowedError,
            tabs.append, Document(),
            )
        return


    def test7(self):
        """Tabs: definition context"""
        import luban
        if luban.has_pyre:
            class MyTabs(luban.e.tabs):

                tab1 = Tab()

                pass
        return
     
    
    
if __name__ == "__main__": unittest.main()

    
# End of file 
