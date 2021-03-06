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


from luban.ui.elements.Element import Element
from luban.ui import elements as lue, actions as lua


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        "element type with same element type name: not allowed"
        import luban
        luban.extension_allow_override = False
        
        class A(Element): 
            abstract = False

        def t():
            class A(Element): 
                abstract = False
            return
        self.assertRaises(A.TypeConflict, t)

        def t2():
            class B(Element): 
                abstract = False
                __unique_type_name__ = 'A'
            return
        self.assertRaises(A.TypeConflict, t2)
        return
     
    
    def test2(self):
        "override by extension"
        import luban
        luban.extension_allow_override = True
        
        class A(Element): 
            abstract = False

        def t():
            class A(Element): 
                abstract = False
            return
        t()

        def t2():
            class B(Element): 
                abstract = False
                __unique_type_name__ = 'A'
            return
        t2()
        return
     
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
