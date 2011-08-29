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


import luban.ui as lui


import unittest
class TestCase(unittest.TestCase):

    def test0(self):
        examples = lui.e.tabs.examples
        code = '\n'.join(examples)
        exec(code)
        return
    
     
    def test1(self):
        tabs = lui.e.tabs()
        tabs.tab().document(title='doc1').paragraph(text='hello')
        tabs.tab().tabs()
        # print(tabs)
        return


    def test2(self):
        tabs = lui.e.tabs()
        self.assertRaises(AttributeError, getattr, tabs, 'document')
        return


    def test3(self):
        tabs = lui.e.tabs()
        tab1 = tabs.tab(id='tab1')
        selecttab1 = lui.a.select(element=tab1).select()
        print(selecttab1)
        return


    def test4(self):
        tabs = lui.e.tabs()
        tab1 = tabs.tab(id='tab1')
        from luban.ui.descriptors.Descriptor import Descriptor
        self.assert_(isinstance(tab1.__class__.onselect, Descriptor))
        tab1.onselect = lui.a.alert("hello")
        from luban.ui.actions.Action import Action
        self.assert_(isinstance(tab1.onselect, Action))
        return


    
if __name__ == "__main__": unittest.main()

    
# End of file 
