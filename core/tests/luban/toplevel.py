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


import luban
print(luban.py_major_ver)

import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        assert luban.a == luban.actions
        assert luban.e == luban.elements
        return


    def test2(self):
        doc = luban.elements.document(title='title')
        return
     
    
if __name__ == "__main__": unittest.main()
    
# End of file 
