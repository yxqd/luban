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


from luban.ui.meta.DescriptorCollector import DescriptorCollector, STORE_NAME
from luban.ui import descriptors
from luban.ui import schema


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        class A(metaclass=DescriptorCollector):
            s = descriptors.str()
            pass
        store = getattr(A, STORE_NAME)
        
        self.assertEqual(len(store), 1)
        self.assertEqual(list(store.values())[0].type, schema.str)
        return
     
    
    def test2(self):
        class A(metaclass=DescriptorCollector):
            s = descriptors.str()
            pass
        class B(A):
            s = descriptors.int()
            pass
        
        store = getattr(B, STORE_NAME)
        
        self.assertEqual(len(store), 1)
        self.assertEqual(list(store.values())[0].type, schema.int)
        return
     
    
    def test3(self):
        class A(metaclass=DescriptorCollector):
            s = descriptors.str()
            pass
        class B(A):
            i = descriptors.int()
            pass

        # A
        store = getattr(A, STORE_NAME)
        
        self.assertEqual(len(store), 1)
        self.assertEqual(list(store.values())[0].type, schema.str)


        # B
        store = getattr(B, STORE_NAME)
        
        self.assertEqual(len(store), 2)
        names = list(store.keys())
        self.assert_('s' in names)
        self.assert_('i' in names)
        
        return
     
    
    def test4(self):
        class C(metaclass=DescriptorCollector):
            s = descriptors.str()
            pass
        c = C()
        self.assertEqual(c.s, '')
        c.s = 'a'
        self.assertEqual(c.s, 'a')
        return
     

if __name__ == "__main__": unittest.main()
    

# End of file 
