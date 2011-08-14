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


from luban.ui import elements as lue


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


    
if __name__ == "__main__": unittest.main()

    
# End of file 
