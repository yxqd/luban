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


from luban.ui.actions.ElementActionBase import ElementActionBase
from luban.ui import e as lue, actions as lua


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        "action type with same type name: not allowed"
        import luban
        luban.extension_allow_override = False
        class A(ElementActionBase): 
            abstract = False
            factory_method = "a"
        def t():
            class A(ElementActionBase): 
                abstract = False
                factory_method = "a2"
            return
        self.assertRaises(A.TypeConflict, t)

        class B(ElementActionBase): 
            abstract = False
            factory_method = "b"
            element_type = lue.document.type
        def t():
            class B(ElementActionBase): 
                abstract = False
                factory_method = "b2"
                element_type = lue.document.type
            return
        self.assertRaises(B.TypeConflict, t)
        return
     
    
    def test2(self):
        "action type with same factory method name: not allowed"
        import luban
        luban.extension_allow_override = False
        class C(ElementActionBase): 
            abstract = False
            factory_method = "c"
        def t():
            class C2(ElementActionBase): 
                abstract = False
                factory_method = "c"
            return
        self.assertRaises(C.ActionFactoryMethodConflict, t)

        class D(ElementActionBase): 
            abstract = False
            factory_method = "d"
            element_type = lue.document.type
        def t():
            class D2(ElementActionBase): 
                abstract = False
                factory_method = "d"
                element_type = lue.document.type
            return
        self.assertRaises(D.ActionFactoryMethodConflict, t)
        return
     
    
    def test3(self):
        "new action type: allowed"
        import luban
        luban.extension_allow_override = False
        class E(ElementActionBase): 
            abstract = False
            factory_method = "e"
        def t():
            class E2(ElementActionBase): 
                abstract = False
                factory_method = "e2"
            return
        t()
        return


    def test4(self):
        "change override option to allow override"
        import luban
        luban.extension_allow_override = True
        class F(ElementActionBase): 
            abstract = False
            factory_method = "f"
        def t():
            class F(ElementActionBase): 
                abstract = False
                factory_method = "f"
                attr1 = descriptors.str()
            return
        t()
        return
     
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
