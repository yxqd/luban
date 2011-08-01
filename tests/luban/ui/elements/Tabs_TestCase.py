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
        tabs.tab(name='tab1')

        tabs.append(Tab(name="tab2"))

        from luban.ui.elements.Document import Document
        self.assertRaises(
            tabs.SubelementDisallowedError,
            tabs.append, Document(),
            )
        return


    def test2(self):
        """Tabs: definition context"""
        import luban.ui.elements as lue
        class MyTabs(lue.tabs):
            
            tab1 = tab()
            
            pass
        return
     
    
    
def main():
    import journal
    # journal.debug('luban.content.ElementContainer').activate()
    unittest.main()
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
