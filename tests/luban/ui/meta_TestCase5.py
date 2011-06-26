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


from pyre.components.Actor import Actor as metabase
class Meta1(metabase):

    @classmethod
    def __prepare__(cls, *args, **kwds):
        print ("meta1", cls)
        return dict()


class SomeClass: pass
class SomeClass2: pass


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        import pyre
        class A(pyre.component, metaclass=Meta1): pass
        class B(A): pass
        return
     

    def test2(self):
        import pyre
        class A(pyre.component, SomeClass, metaclass=Meta1): pass
        class B(A): 
            s = pyre.properties.str()
            pass
        b = B()
        self.assertEqual(b.s, '')
        return
     

    def test3(self):
        import pyre
        class A(pyre.component, SomeClass, metaclass=Meta1): pass
        class B(A, SomeClass2): pass
        class C(B):
            s = pyre.properties.str()
        c = C()
        self.assertEqual(c.s, '')
        c.s = 'a'
        self.assertEqual(c.s, 'a')
        return
     

if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 
