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


import unittest

class TestCase(unittest.TestCase):


    def test(self):
        import luban.ui.elements as lue
        
        frame = lue.frame(name='frame', title="title")
        
        header = frame.document(name='header')
        sp = lue.splitter(name="sp"); header.append(sp)
        self.assert_(len(header.contents) == 1)
        
        body = frame.document(name='body', title="body")
        
        self.assert_(header.contents is not None)
        self.assert_(len(header.contents) > 0)
        
        return
     
    
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
