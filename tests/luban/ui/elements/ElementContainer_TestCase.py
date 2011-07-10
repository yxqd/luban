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
