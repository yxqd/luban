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


import unittest
class TestCase(unittest.TestCase):

    def test1(self):

        # create a document
        doc = luban.e.document()

        # form is not available right now
        self.assertRaises(AttributeError, getattr, doc, 'form')
        self.assertRaises(AttributeError, getattr, luban.e, 'form')

        # extension
        import extension_example
        # now we should have form available
        form = doc.form()
        form2 = luban.e.form()

        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
