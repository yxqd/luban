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


from luban.ui.AttributeContainer import Meta, AttributeContainer

class SomeClass: pass
class SomeClass2: pass


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        import pyre
        class A(AttributeContainer): 
            s = pyre.properties.str()
            s1 = descriptors.str()
        a = A()
        self.assertEqual(a.s, '')
        a.s = 's'
        self.assertEqual(a.s, 's')

        self.assertEqual(a.s1, '')
        a.s1 = 's1'
        self.assertEqual(a.s1, 's1')
        return
     

    def test2(self):
        import pyre
        class E(AttributeContainer): 
            s = pyre.properties.str()
            s1 = descriptors.str()
        class EC(E, SomeClass):
            s2 = descriptors.str()

        a = EC()
        self.assertEqual(a.s, '')
        a.s = 's'
        self.assertEqual(a.s, 's')

        self.assertEqual(a.s1, '')
        a.s1 = 's1'
        self.assertEqual(a.s1, 's1')

        self.assertEqual(a.s2, '')
        a.s2 = 's2'
        self.assertEqual(a.s2, 's2')
        return
     

    def test3(self):
        import pyre
        class E(AttributeContainer): 
            s = pyre.properties.str()
            s1 = descriptors.str()
        class EC(E, SomeClass, predefined={'i': 1}):
            self.assertEqual(i, 1)

        a = EC()
        self.assertEqual(a.s, '')
        a.s = 's'
        self.assertEqual(a.s, 's')

        self.assertEqual(a.s1, '')
        a.s1 = 's1'
        self.assertEqual(a.s1, 's1')

        return
     

    def test4(self):
        import pyre
        class E(AttributeContainer): 
            s = pyre.properties.str()
            s1 = descriptors.str()
        from luban.ui.PredefinedSymbols import PredefinedSymbols
        class predefined(PredefinedSymbols):
            def __missing__(self, key):
                if key == 'abc':
                    return key
                raise KeyError(key)
            
        class EC(E, SomeClass, predefined=predefined()):
            self.assertEqual(abc, 'abc')
            self.assert_(descriptors is not None)

        a = EC()
        self.assertEqual(a.s, '')
        a.s = 's'
        self.assertEqual(a.s, 's')
        
        self.assertEqual(a.s1, '')
        a.s1 = 's1'
        self.assertEqual(a.s1, 's1')

        return
     

    def test5(self):
        import pyre
        class E(AttributeContainer): 
            s = pyre.properties.str()
            s1 = descriptors.str()
        from luban.ui.PredefinedSymbols import PredefinedSymbols
        class predefined(PredefinedSymbols):
            def __missing__(self, key):
                if key == 'abc':
                    return key
                raise KeyError(key)
            
        class EC(E, SomeClass, predefined=predefined()):
            self.assertEqual(abc, 'abc')
            self.assert_(descriptors is not None)

        class D(EC):
            self.assert_(descriptors is not None)
            self.assertEqual(abc, 'abc')
            
        return


if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
