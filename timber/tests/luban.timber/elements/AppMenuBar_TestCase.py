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
        m1 = appmenubar.menu(name="m1")
        i1 = appmenubar.item(name="i1")

        m1.menu(name="m11")
        m1.item(name="i12")

        from luban.ui.elements.Document import Document
        self.assertRaises(
            appmenubar.SubelementDisallowedError, 
            appmenubar.append, Document())
        self.assertRaises(
            appmenubar.SubelementDisallowedError,
            m1.append, Document())
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
