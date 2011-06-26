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


def createDict(bases):

    a = dict()
        
    for base in bases:
        if hasattr(base, "getSubclassPreparationContext"):
            c = base.getSubclassPreparationContext()
            a.update(c)
        continue
        
    return a



from pyre.patterns.AbstractMetaclass import AbstractMetaclass
class AttributeClassifier(AbstractMetaclass):

    @classmethod
    def __prepare__(cls, name, bases, **kwds):
        d = super().__prepare__(name, bases, **kwds)
        d.update(createDict(bases))
        return d
                 

    def __new__(cls, name, bases, attributes, **kwds):
        instance = super().__new__(cls, name, bases, dict(attributes))
        return instance
                 

class Component(metaclass=AttributeClassifier):
                     
    pass



import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        class A(Component):
            @classmethod
            def getSubclassPreparationContext(cls):
                return {'a': 1}

        class B(A):
            self.assertEqual(a, 1)
            
        return
     
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
