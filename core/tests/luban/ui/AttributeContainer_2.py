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


from luban import py_major_ver, setup_context
if py_major_ver == 2:
    setup_context(locals())
    

from luban.ui.AttributeContainer import Meta, AttributeContainer

class SomeClass: pass
class SomeClass2: pass


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        "descriptor: get, set"
        class A(AttributeContainer): 
            s = descriptors.str()
            s1 = descriptors.str()
        a = A()
        self.assertEqual(a.s, None)
        a.s = 's'
        self.assertEqual(a.s, 's')

        self.assertEqual(a.s1, None)
        a.s1 = 's1'
        self.assertEqual(a.s1, 's1')
        return
     

if __name__ == "__main__": unittest.main()

    
# End of file 
