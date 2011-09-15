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

    def test0a(self):
        print (luban.e.splitter.getCtorDocStr())
        print (luban.e.splitter.__init__.__doc__)
        print (luban.e.document.__init__.__doc__)
        return
    
     
if __name__ == "__main__": unittest.main()

    
# End of file 
