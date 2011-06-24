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


from pyre.components.Actor import Actor
class Meta1(Actor):

    def __prepare__(cls, *args, **kwds):
        return dict()


import pyre
class Element(pyre.component, metaclass=Meta1):

    s = pyre.properties.str()
    


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        e = Element()
        self.assertEqual(e.s, '')
        return
     
    
if __name__ == "__main__": unittest.main()
    
# version
__id__ = "$Id$"

# End of file 
