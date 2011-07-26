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
        """luban.content.ElementContainer: allowed_element_types: Accordion"""
        from luban.ui.elements.Accordion import Accordion, AccordionSection
        accordion = Accordion()
        accordion.section()

        accordion.append(AccordionSection(name='s1'))

        from luban.ui.elements.Document import Document
        self.assertRaises(
            accordion.SubelementDisallowedError, 
            accordion.append, 
            Document(name="doc"),
            )
        return


    def test2(self):
        from luban.ui.elements.Accordion import Accordion
        class Myaccordion(Accordion):
            
            s1 = section()

        ma = Myaccordion()
        ma.s1
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
