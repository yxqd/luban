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
        from luban.ui.elements._registry import isElementFacility
        from luban.ui.descriptors import element
        e = element()
        self.assert_(isElementFacility(e))
        return


    def test2(self):
        from luban.ui.elements._registry import registerAllElements
        import luban.ui.elements as lue
        registerAllElements(lue)
        return

    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
