#!/usr/bin/env python3
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


import unittest

class TestCase(unittest.TestCase):

    def test4(self):
        """luban.content.ElementContainer: allowed_element_types: AppMenuBar"""
        from luban.ui.elements.AppMenuBar import AppMenuBar
        appmenubar = AppMenuBar()
        m1 = appmenubar.menu()
        i1 = appmenubar.item()

        m1.menu()
        m1.item()

        from luban.ui.elements.Document import Document
        self.assertRaises(ValueError, appmenubar.append, Document())
        self.assertRaises(ValueError, m1.append, Document())
        return


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
    # journal.debug('luban.content.ElementContainer').activate()

    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
