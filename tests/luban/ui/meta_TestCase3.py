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


class Meta1(type):

    @classmethod
    def __prepare__(cls, *args, **kwds):
        import pdb; pdb.set_trace()
        print ("meta1", cls)
        return dict()



import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        class A(metaclass=Meta1): pass
        class B(A): pass
        return
     

    def test2(self):
        class A(metaclass=Meta1): pass
        class B: pass
        class C(A, B): pass
        class D(B, A): pass
        return
     
     
    def test3(self):
        class A(metaclass=Meta1): pass
        class B: pass
        class C(A): pass
        class D(C, B): pass
        return
     
     
    
if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 
