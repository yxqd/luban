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


import luban
import luban.timber

import unittest
class TestCase(unittest.TestCase):

    def test0(self):
        frame = luban.e.frame()
        frame.form()
        return
     
    def test1(self):
        frame = luban.e.frame()
        form = frame.form()
        form.onsubmit = luban.a.load(actor='actor', routine='routine', kwds=luban.event.data)
        button = frame.button(onclick=luban.a.select(id='').append(newelement=form))
        return

    
if __name__ == "__main__": unittest.main()

    
# End of file 
