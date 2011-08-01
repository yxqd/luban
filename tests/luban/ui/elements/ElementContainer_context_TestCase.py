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
        from luban.ui.elements.ElementContainer import ElementContainer
        class T(ElementContainer):
            
            t = descriptors

        return


    def test3(self):
        from luban.ui.elements.ElementContainer import ElementContainer, Meta
        class T(ElementContainer):
            
            d = Document()

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
