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
        "subclass definition: section"
        from luban.ui.elements.Accordion import Accordion
        class Myaccordion(Accordion):
            
            s1 = Section()

        ma = Myaccordion()
        ma.s1
        return


    def test2a(self):
        "subclass definition: document disallowed"
        from luban.ui.elements.Accordion import Accordion
        class Myaccordion(Accordion):
            
            try:
                d1 = Document()
            except NameError:
                pass
            else:
                raise RuntimeError("should throw NameError")

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
