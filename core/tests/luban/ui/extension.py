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

import luban
try:
    luban.e.form
except AttributeError:
    pass
else:
    m = "form should not have been defined"
    raise RuntimeError(m)

try:
    luban.a.reboot
except AttributeError:
    pass
else:
    m = "reboot should not have been defined"
    raise RuntimeError(m)

# extension kicks in
import extension_example
# and form is available
luban.e.form
# and reboot is available
luban.a.reboot


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        # create a form
        form = luban.e.form(id='login')
        # the submit event handler
        form.onsubmit = luban.a.select(element=form).submit(actor="login", routine="verify")
        return

    
    def test2(self):
        r = luban.a.reboot()
        # print(r)
        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
