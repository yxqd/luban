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


from luban import setup_context
setup_context(locals())
    

from luban.ui.AttributeContainer import Meta, AttributeContainer

class SomeClass: pass
class SomeClass2: pass


import unittest
class TestCase(unittest.TestCase):
     
    def test2(self):
        "inheritance and descriptors"
        class E(AttributeContainer): 
            s = descriptors.str()
            s1 = descriptors.str()
            
        class EC(SomeClass, E):
            __metaclass__=Meta
            s2 = descriptors.str()

        a = EC()
        self.assertEqual(a.s, None)
        a.s = 's'
        self.assertEqual(a.s, 's')

        self.assertEqual(a.s1, None)
        a.s1 = 's1'
        self.assertEqual(a.s1, 's1')

        self.assertEqual(a.s2, None)
        a.s2 = 's2'
        self.assertEqual(a.s2, 's2')
        return
     

if __name__ == "__main__": unittest.main()

    
# End of file 
