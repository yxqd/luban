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


from luban import ui as lui
import extension_example


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        form = lui.e.form(id='login')
        form.onsubmit = lui.a.select(element=form).submit(actor="login", routine="verify")
        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
