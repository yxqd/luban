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
        from luban.controller.ControllerBase import ControllerBase
        c = ControllerBase("actors")
        c._retrieveActor('default')
        return
     
    
if __name__ == "__main__": unittest.main()
    
# End of file 