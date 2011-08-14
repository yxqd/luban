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


from luban.ui.elements.SubElementFactory import SubElementFactory


import unittest
class TestCase(unittest.TestCase):

    def test0(self):
        "SubElementFactory"
        f = SubElementFactory()
        self.assertRaises(AttributeError, getattr, f, 'a')
        return


    def test1(self):
        "SubElementFactory"
        from luban.ui.elements.Document import Document
        d = Document()
        f = d.document
        d2 = f()
        self.assertEqual(len(d.contents), 1)
        self.assertEqual(d.contents[0], d2)

        # frame is not allowed as a sub element
        self.assertRaises(AttributeError, getattr, d, 'frame')

        # tab is not allowed as a sub element
        self.assertRaises(AttributeError, getattr, d, 'tab')

        # tabs, paragraph are allowd
        d.tabs
        d.paragraph
        return

    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
