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
        """ order of descriptors
        """
        from luban.ui.AttributeContainer import AttributeContainer
        class A(AttributeContainer):
            
            # s = AttributeContainer.descriptors.str('a')
            s1 = descriptors.str('s1')
            a2 = d.str('a2')
            a1 = d.str('a1')
            
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
