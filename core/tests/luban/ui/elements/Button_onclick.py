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

from luban.ui import e as lue, a as lua


import unittest

class TestCase(unittest.TestCase):

    def test1(self):
        b = lue.button()
        b.onclick = lua.alert("hey")
        self.assert_(b.onclick is not None)
        return
     
    
    def test2(self):
        d = lue.document()
        
        b = lue.button(); d.append(b)
        b.onclick = lua.alert("hey")
        self.assert_(b.onclick is not None)
        
        d1 = lue.document(onclick=None)
        self.assert_(b.onclick is not None)
        return
     

    def test3(self):
        doc1 = lue.document(name='doc1')
        doc1.onclick = lua.alert('a')
        self.assert_(doc1.onclick is not None)
        
        doc2 = lue.document(name='doc2')
        self.assert_(doc1.onclick is not None)

        return
        
        
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
