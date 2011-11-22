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
        from luban.controller import decorators
        @decorators.typeconversion()
        def f(b: decorators.bool=None, i: decorators.int=None):
            print (b,i)
            return
        f('false', '10')
        return
     
    
    def test2(self):
        from luban.controller import decorators
        class A:
            @decorators.typeconversion()
            def f(self, b: decorators.bool=None, i: decorators.int=None):
                print (self, b,i)
                return
        A().f('false', '10')
        return
     
    
    def test3(self):
        from luban.controller import decorators
        class A:
            @decorators.typeconversion()
            def f(self, b: decorators.bool=None, i: decorators.int=None, **kwds):
                print (self, b,i, kwds)
                return
        A().f('false', '10', t=3)
        return
     
    
if __name__ == "__main__": unittest.main()
    
# End of file 
