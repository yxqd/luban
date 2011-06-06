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
        """metaclass __prepare__
        """
        class Meta(type):
            @classmethod
            def __prepare__(cls, name, bases, **kwds):
                d = dict()
                d['hey'] = 1
                return d

        class A(metaclass=Meta):
            
            self.assertEqual(hey, 1)

        print(A.hey)
        return
     
    
if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 
