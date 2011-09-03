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


from luban import ui as lui


import unittest
class TestCase(unittest.TestCase):


    def test(self):
        frame = lui.e.frame(name='frame', title="title")
        
        header = frame.document(name='header')
        subdoc = lui.e.document(name="subdoc"); header.append(subdoc)
        self.assert_(len(header.contents) == 1)
        
        body = frame.document(name='body', title="body")
        
        self.assert_(header.contents is not None)
        self.assert_(len(header.contents) > 0)
        
        return
     
    
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
