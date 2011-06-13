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
        from luban.ui.elements.Element import Element
        return
     
    
    def test2(self):
        from luban.ui.elements.Element import Element
        name = "e1"
        
        e1 = Element(name=name)
        self.assertEqual(e1.name, name)
        
        Class = "class"
        e2 = Element(name=name, Class=Class)
        self.assertEqual(e2.Class, Class)
        
        print(list(e2.iterAttributes()))
        return
     
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
