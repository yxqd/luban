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
            s1 = descriptors.str()
            a2 = d.str()
            a1 = d.str()
            
            pass
        
        # make sure order is preserved
        self.assertEqual(
            list(d.name for d in A.iterDescriptors()),
            ['s1', 'a2', 'a1']
            )
        
        return
     
    
    def test2(self):
        """ attribute
        """
        from luban.ui.AttributeContainer import AttributeContainer
        class A(AttributeContainer):
            
            s1 = descriptors.str()
            a2 = d.str()
            a1 = d.str()
            
            pass
        
        a = A()

        self.assertEqual(a.s1, '')
        a.s1 = 5
        self.assertEqual(a.s1, '5')
        return
     
    
if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 
