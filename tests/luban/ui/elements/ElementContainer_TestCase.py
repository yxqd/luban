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

    def test0(self):
        "_iterDeclaredSubElements"
        from luban.ui.elements.ElementContainer import ElementContainer
        c = ElementContainer()
        self.assert_(len(list(c._iterDeclaredSubElements()))==0)
        return


    def test0a(self):
        "_iterDeclaredSubElements case 2"
        from luban.ui.elements.ElementContainer import ElementContainer
        from luban.ui.elements.Element import Element

        class C(ElementContainer):
            sub1 = descriptors.element(default=Element)
        c = C()

        subelems = list(c._iterDeclaredSubElements())
        self.assert_(len(subelems)==1)
        self.assert_(subelems[0] == c.sub1)
        return
    
     
    def _test1(self):
        """luban.content.ElementContainer: allowed_element_types: Splitter"""
        splitter = Splitter()
        splitter.section()

        splitter.add(SplitSection())

        self.assertRaises(ValueError, splitter.add, Document())
        return
     
    
    def _test2(self):
        """luban.content.ElementContainer: allowed_element_types: Tabs"""
        tabs = Tabs()
        tabs.tab()

        tabs.add(Tab())

        self.assertRaises(ValueError, tabs.add, Document())
        return
     
    
    def _test3(self):
        """luban.content.ElementContainer: allowed_element_types: Accordion"""
        accordion = Accordion()
        accordion.section()

        accordion.add(AccordionSection())

        self.assertRaises(ValueError, accordion.add, Document())
        return


    def _test4(self):
        """luban.content.ElementContainer: allowed_element_types: AppMenuBar"""
        appmenubar = AppMenuBar()
        m1 = appmenubar.menu()
        i1 = appmenubar.item()

        m1.menu()
        m1.item()

        self.assertRaises(ValueError, appmenubar.add, Document())
        self.assertRaises(ValueError, m1.add, Document())
        return


    def _test5(self):
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
    # journal.debug('luban.content.ElementContainer').activate()

    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
