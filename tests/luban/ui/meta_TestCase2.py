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


from pyre.components.Actor import Actor
class Meta1(Actor):

    def __prepare__(cls, *args, **kwds):
        # return dict()
        from luban.ui.OrderedDictWithPredefinedSymbols import OrderedDictWithPredefinedSymbols
        d = OrderedDictWithPredefinedSymbols()
        return d


import pyre
class Element(pyre.component, metaclass=Meta1):

    s = pyre.properties.str()


class Meta2(Meta1): pass
class Element2(Element, metaclass=Meta2):
    
    a = pyre.properties.float()
    


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        e = Element()
        self.assertEqual(e.s, '')
        return
     
    
    def test2(self):
        e = Element2()
        self.assertEqual(e.a, 0)
        return
     
    
if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 