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
        from luban.ui.actions.Loading import Loading
        return
     
    
    def test2(self):
        from luban.ui.actions import load
        action = load(actor="actor", routine="routine", a=3, b="b")
        self.assertEqual(action.actor, "actor")
        self.assertEqual(action.routine, "routine")
        self.assertEqual(action.params, {'a': 3, "b": "b"})
        return
     
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
