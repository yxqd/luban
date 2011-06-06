#!/usr/bin/env python3
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        from luban.ui.elements.AttributeContainer import AttributeContainer
        class A(AttributeContainer):
            
            # s = AttributeContainer.descriptors.str('a')
            s1 = properties.str('s1')
            a2 = p.str('a2')
            a1 = p.str('a1')
            
            pass
        
        # make sure order is preserved
        self.assertEqual(
            list(d.name for d in A.iterDescriptors()),
            ['s1', 'a2', 'a1']
            )
        
        return
     
    
if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 
