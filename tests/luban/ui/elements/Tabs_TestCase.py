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

    def test1(self):
        """luban.content.ElementContainer: allowed_element_types: Tabs"""
        from luban.ui.elements.Tabs import Tabs, Tab
        tabs = Tabs()
        tabs.tab()

        tabs.append(Tab())

        from luban.ui.elements.Document import Document
        self.assertRaises(ValueError, tabs.append, Document())
        return


    def test2(self):
        """Tabs: definition context"""
        import luban.ui.elements as lue
        class MyTabs(lue.tabs):
            pass
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
