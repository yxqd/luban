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
        from luban.ui.elements.Paragraph import Paragraph
        p = Paragraph(text='hello world')
        self.assertEqual(p.text, 'hello world')
        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
