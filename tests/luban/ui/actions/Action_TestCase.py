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
     
    
    def test3(self):
        from luban.ui.actions.Action import Action
        a1 = Action(name='a1')
        a2 = Action(name='a2')
        import pyre
        self.assertRaises(
            pyre.schema.exceptions.CastingError,
            setattr, a1, 'onfinish', 3)
        a1.onfinish = a2
        return
     
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
