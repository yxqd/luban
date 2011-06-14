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
        from luban.ui.actions.Action import Action
        return
     
    
    def test2(self):
        from luban.ui.actions.Action import Action
        name = "a1"
        
        a1 = Action(name=name)
        self.assertEqual(a1.name, name)
        
        return
     
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
