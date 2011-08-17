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


import unittest
class TestCase(unittest.TestCase):

    def test1(self):

        # create a document
        doc = lui.e.document()

        # form is not available right now
        self.assertRaises(AttributeError, getattr, doc, 'form')
        self.assertRaises(AttributeError, getattr, lui.e, 'form')

        # extension
        import extension_example
        # now we should have form available
        form = doc.form()
        form2 = lui.e.form()

        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
