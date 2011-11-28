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
import luban.timber

import unittest
class TestCase(unittest.TestCase):

    def test0(self):
        frame = luban.e.frame()
        doc = frame.document()

        frame.dialog()
        
        doc = frame.document()
        self.assertRaises(AttributeError, getattr, doc, 'dialog')
        
        return
     
    
    
if __name__ == "__main__": unittest.main()

    
# End of file 
