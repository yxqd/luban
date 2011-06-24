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
        """dict(...)
        """
        from luban.ui.OrderedDictWithPredefinedSymbols import OrderedDictWithPredefinedSymbols
        d = OrderedDictWithPredefinedSymbols()
        d1 = dict(d)
        return
     
    
    def test2(self):
        """update
        """
        from luban.ui.OrderedDictWithPredefinedSymbols import OrderedDictWithPredefinedSymbols
        d = OrderedDictWithPredefinedSymbols()
        
        d1 = {'a':3}
        d.update(d1)

        d1.update(d)
        return
     
    
if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 
