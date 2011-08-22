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


from luban.ui import e as lue, actions as lua


import unittest
class TestCase(unittest.TestCase):

    def test0(self):
        examples = lue.tabs.examples
        code = '\n'.join(examples)
        exec(code)
        return
    
     
    def test1(self):
        tabs = lue.tabs()
        tabs.tab().document(title='doc1').paragraph(text='hello')
        tabs.tab().tabs()
        # print(tabs)
        return


    def test2(self):
        tabs = lue.tabs()
        self.assertRaises(AttributeError, getattr, tabs, 'document')
        return


    def test3(self):
        tabs = lue.tabs()
        tab1 = tabs.tab(id='tab1')
        selecttab1 = lua.select(element=tab1).select()
        print(selecttab1)
        return


    
if __name__ == "__main__": unittest.main()

    
# End of file 
