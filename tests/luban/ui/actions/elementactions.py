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


from luban.ui import actions as lua, elements as lue

import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        new = lue.document(title="new")
        action = lua.select(id="abc").replaceContent(new)
        print (action)
        return
     
    
if __name__ == "__main__": unittest.main()


# version
__id__ = "$Id$"

# End of file 
