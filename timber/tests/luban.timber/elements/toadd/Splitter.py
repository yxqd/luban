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
        """Splitter: allowed sub elements"""
        from luban.ui.elements.Splitter import Splitter, SplitSection
        splitter = Splitter()

        splitter.section(name='sec1', id='sec1')

        splitter.append(SplitSection(name='sec2', id='sec2'))

        from luban.ui.elements.Document import Document
        self.assertRaises(
            splitter.SubelementDisallowedError,
            splitter.append, Document())
        
        # self.assertEqual(splitter.contents[0].id, 'sec1')
        self.assertEqual(splitter.contents[1].id, 'sec2')
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
