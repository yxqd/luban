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


from luban.ui import elements as lue


import unittest
class TestCase(unittest.TestCase):

    def test1(self):

        # create a document
        doc = lue.document()

        # form is not available right now
        self.assertRaises(AttributeError, getattr, doc, 'form')
        self.assertRaises(AttributeError, getattr, lue, 'form')

        # extension
        import extension_example
        self.assertRaises(AttributeError, getattr, doc, 'form')
        self.assertRaises(AttributeError, getattr, lue, 'form')
        
        # register the extension
        lue.registerElementProvider(extension_example)
        
        # now we should have form available
        form = doc.form()
        form2 = lue.form()

        return
     
    
if __name__ == "__main__": unittest.main()

    
# End of file 
