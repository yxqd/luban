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


from pyre.patterns.AbstractMetaclass import AbstractMetaclass
class AttributeClassifier(AbstractMetaclass):

    @classmethod
    def __prepare__(cls, name, bases, predefined=None, **kwds):
        from luban.ui.OrderedDictWithPredefinedSymbols import OrderedDictWithPredefinedSymbols
        d = OrderedDictWithPredefinedSymbols()
        d.predefined = predefined
        return d


    def __new__(cls, name, bases, attributes, **kwds):
        instance = super().__new__(cls, name, bases, dict(attributes))
        return instance


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        predefined = {'a': 1}
        class A(metaclass=AttributeClassifier, predefined=predefined):
            self.assertEqual(a, 1)

        predefined = {'b': 1}
        class A(metaclass=AttributeClassifier, predefined=predefined):
            self.assertEqual(b, 1)
        return
     
    
if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 
