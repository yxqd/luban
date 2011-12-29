#!/usr/bin/env python
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


import luban.timber, luban


import unittest
class TestCase(unittest.TestCase):

    def test0(self):
        pb = luban.e.progressbar()
        self.assertRaises(ValueError, getattr, pb, 'onchecking')
        return
     
    
    
if __name__ == "__main__": unittest.main()

    
# End of file 
