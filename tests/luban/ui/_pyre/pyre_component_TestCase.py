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

from luban.ui import elements as lue, actions as lua


import unittest

class TestCase(unittest.TestCase):

    def test1(self):
        import pyre
        class C(pyre.component):
            
            a = pyre.components.properties.object()

        c1 = C(); c1.a = 'a'
        self.assertEqual(c1.a, 'a')

        c2 = C(); c2.a = None
        
        self.assertEqual(c1.a, 'a')
        self.assertEqual(c2.a, None)
        return


if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 