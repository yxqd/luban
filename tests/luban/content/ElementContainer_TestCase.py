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


from luban.content.Page import Page
from luban.content.Document import Document
from luban.content.Splitter import Splitter, SplitSection
from luban.content.Tabs import Tabs, Tab
from luban.content.Accordion import Accordion, AccordionSection
from luban.content.AppMenuBar import AppMenuBar, AppMenu, AppMenuItem

import unittest

class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban.content.ElementContainer: allowed_element_types: Splitter"""
        splitter = Splitter()
        splitter.section()

        splitter.add(SplitSection())

        self.assertRaises(ValueError, splitter.add, Document())
        return
     
    
    def test2(self):
        """luban.content.ElementContainer: allowed_element_types: Tabs"""
        tabs = Tabs()
        tabs.tab()

        tabs.add(Tab())

        self.assertRaises(ValueError, tabs.add, Document())
        return
     
    
    def test3(self):
        """luban.content.ElementContainer: allowed_element_types: Accordion"""
        accordion = Accordion()
        accordion.section()

        accordion.add(AccordionSection())

        self.assertRaises(ValueError, accordion.add, Document())
        return


    def test4(self):
        """luban.content.ElementContainer: allowed_element_types: AppMenuBar"""
        appmenubar = AppMenuBar()
        m1 = appmenubar.menu()
        i1 = appmenubar.item()

        m1.menu()
        m1.item()

        self.assertRaises(ValueError, appmenubar.add, Document())
        self.assertRaises(ValueError, m1.add, Document())
        return


    def test5(self):
        """luban.content.ElementContainer: disallowed_element_types: Page"""
        page = Page()
        document = Document()
        self.assertRaises(ValueError, document.add, page)
        return
     
    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
    journal.debug('luban.content.ElementContainer').activate()

    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
