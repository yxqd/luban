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


    def test1(self):
        "ElementContainer.remove"
        frame = luban.e.frame(name='frame', title="title")
        doc = frame.document()
        self.assertEqual(len(frame.contents), 1)
        
        frame.remove(doc)
        self.assertEqual(len(frame.contents), 0)
        return

    
    def test2(self):
        "ElementContainer.replaceChild"
        frame = luban.e.frame(name='frame', title="title")
        doc1 = frame.document()
        self.assertEqual(len(frame.contents), 1)
        self.assertEqual(frame.contents[0], doc1)
        
        doc2 = frame.document()
        self.assertRaises(RuntimeError, frame.replaceChild, doc1, doc2)
        
        doc3 = luban.e.document()
        frame.replaceChild(doc1, doc3)
        self.assertEqual(len(frame.contents), 2)
        self.assertEqual(frame.contents[0], doc3)
        self.assertEqual(frame.contents[1], doc2)
        return

    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
