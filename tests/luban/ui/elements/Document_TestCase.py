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

    def test1(self):
        from luban.ui.elements.Document import Document
        return
     
    
    def test5(self):
        """luban.content.ElementContainer: disallowed_element_types: frame"""
        import luban.ui.elements as lue
        frame = lue.frame()
        document = lue.document()
        self.assertRaises(document.SubelementDisallowedError, document.append, frame)
        return
     
    
    def _test2(self):
        from luban.ui.elements.Document import Document
        class V(Document):
            p = paragraph()
        return
     
    
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
