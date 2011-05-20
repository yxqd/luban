#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def positive(v):
    if v<=0: raise ValueError, "must be positive"
    return v

def positive2(v):
    try:
        v = float(v)
    except:
        raise ValueError, 'must be a float'
    if v<=0: raise ValueError, "must be positive"
    return v

import unittest

class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban.inventory: properties"""
        from pyre.inventory.Inventory import Inventory as base
        class Inventory(base):

            import luban.inventory

            f = luban.inventory.float(name='f', validator=positive)

        i = Inventory('i')
        self.assertEqual(i.f, 0.)

        i.f = 'abc'

        self.assertRaises(ValueError, Inventory.f.convertValue, 'ab')
        self.assertRaises(ValueError, Inventory.f.convertValue, '-3')
        return


    def test2(self):
        """luban.inventory: propertyset"""
        from pyre.inventory.Inventory import Inventory as base
        class Inventory(base):

            import luban.inventory

            import re
            xset = luban.inventory.propertySet(
                name='xset',
                pattern=re.compile('x.*'),
                validator=positive2)

        i = Inventory('i')
        i.x3 = '5'
        i.x4 = 'abc'
        i.x5 = '-3'

        props = i.xset.getPropertyNames()
        props.sort()
        self.assertEqual(props, ['x3', 'x4', 'x5'])
        
        self.assertEqual(
            i.xset.getValueErrors(),
            {'x4': 'must be a float',
             'x5': 'must be positive',
             }
            )
        return
     
    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
