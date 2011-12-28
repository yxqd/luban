#!/usr/bin/env python
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

from luban import setup_context
setup_context(locals())


from luban.ui.AttributeContainer import AttributeContainer

import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        "'action' descriptor"
        class T(AttributeContainer):
            
            a = descriptors.action()
            
            pass

        t = T()
        self.assertRaises(ValueError, setattr, t, 'a', 0)

        t.a = None
        
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
