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


from luban.ui import actions as lua, e as lue

import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        new = lue.document(title="new")
        action = lua.select(id="abc").replaceContent(newcontent=new)
        # print (action)
        return
     
    
    def test2(self):
        container = lue.document(title="container", id='container')
        new = lue.document(title="new")
        action = lua.select(element=container).replaceContent(newcontent=new)
        # print (action)
        return
     
    
if __name__ == "__main__": unittest.main()


# End of file 
