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


import luban

import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        from luban.ui.elements.Document import Document
        return
     
    
    def test2(self):
        """luban.content.ElementContainer: disallowed_element_types: frame"""
        frame = luban.e.frame()
        document = luban.e.document()
        self.assertRaises(
            document.SubelementDisallowedError, 
            document.append, frame,
            )
        return
     
    
    def test3(self):
        import luban
        if luban.has_pyre:
            from luban.ui.elements.Document import Document
            class V(Document):
                p = paragraph()
        return
     
    
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
