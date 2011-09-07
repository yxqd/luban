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

    def test0a(self):
        print (lui.e.splitter.getCtorDocStr())
        print (lui.e.splitter.__init__.__doc__)
        print (lui.e.document.__init__.__doc__)
        return
    
     
if __name__ == "__main__": unittest.main()

    
# End of file 
