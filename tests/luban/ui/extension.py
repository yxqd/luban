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
try:
    lui.e.form
except AttributeError:
    pass
else:
    m = "form should not have been defined"
    raise RuntimeError(m)

# extension kicks in
import extension_example
# and form is available
lui.e.form


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        # create a form
        form = lui.e.form(id='login')
        # the submit event handler
        form.onsubmit = lui.a.select(element=form).submit(actor="login", routine="verify")
        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
