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

    def test1(self):
        tabs = lue.tabs()
        tabs.tab().document(title='doc1').paragraph(text='hello')
        tabs.tab().tabs()
        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
