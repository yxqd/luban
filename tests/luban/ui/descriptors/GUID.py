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
        from luban.ui.AttributeContainer import AttributeContainer
        class A(AttributeContainer):
            id = descriptors.guid()
        a = A()
        a.id = 3
        self.assertEqual(a.id, '3')
        
        a2 = A()
        self.assert_(a2.id is not None)
        self.assert_(len(a2.id))
        return
     

def main():    
    import journal
    journal.debug('metaclass').active = True
    unittest.main()
    return

if __name__ == "__main__": main()
    
# version
__id__ = "$Id$"

# End of file 
