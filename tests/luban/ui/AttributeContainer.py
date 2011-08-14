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
     
    def test0(self):
        """namespace
        """
        from luban.ui.AttributeContainer import AttributeContainer
        class A(AttributeContainer):
            
            self.assert_(descriptors is not None)
            self.assert_(validators is not None)

            self.assertEqual(d, descriptors)
            self.assertEqual(v, validators)
        
        return
     
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
        """descriptor: set and get attribute
        """
        from luban.ui.AttributeContainer import AttributeContainer
        class A(AttributeContainer):
            
            s1 = descriptors.str()
            
            pass
        
        a = A()

        self.assertEqual(a.s1, '')
        a.s1 = 5
        self.assertEqual(a.s1, '5')
        return


    def test3(self):
        "getAttribute, setAttribute"
        from luban.ui.AttributeContainer import AttributeContainer
        class A(AttributeContainer):
            
            s1 = descriptors.str()
            
            pass
        
        a = A()
        
        self.assertEqual(a.getAttribute('s1'), '')
        a.setAttribute('s1', 5)
        self.assertEqual(a.getAttribute('s1'), '5')
        return
     

def main():    
    from luban import journal
    journal.debug('metaclass').active = True
    unittest.main()
    return

if __name__ == "__main__": main()
    
# version
__id__ = "$Id$"

# End of file 
