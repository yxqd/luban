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
    
     
    def test0b(self):
        from luban.ui.elements.ElementContainer import ElementContainer
        import luban.ui.elements.Document
        class E(ElementContainer):
            d = document()
        return
     
    
    def test1(self):
        """luban.content.ElementContainer: allowed_element_types: Splitter"""
        from luban.ui.elements.Splitter import Splitter, SplitSection
        splitter = Splitter()
        splitter.section()

        splitter.append(SplitSection())

        from luban.ui.elements.Document import Document
        self.assertRaises(ValueError, splitter.append, Document())
        return
     
    
    def test2(self):
        """luban.content.ElementContainer: allowed_element_types: Tabs"""
        from luban.ui.elements.Tabs import Tabs, Tab
        tabs = Tabs()
        tabs.tab()

        tabs.append(Tab())

        from luban.ui.elements.Document import Document
        self.assertRaises(ValueError, tabs.append, Document())
        return
     
    
    def test3(self):
        """luban.content.ElementContainer: allowed_element_types: Accordion"""
        from luban.ui.elements.Accordion import Accordion, AccordionSection
        accordion = Accordion()
        accordion.section()

        accordion.append(AccordionSection())

        from luban.ui.elements.Document import Document
        self.assertRaises(ValueError, accordion.append, Document())
        return


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


    def test5(self):
        """luban.content.ElementContainer: disallowed_element_types: frame"""
        import luban.ui.elements as lue
        frame = lue.frame()
        document = lue.document()
        self.assertRaises(ValueError, document.append, frame)
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
