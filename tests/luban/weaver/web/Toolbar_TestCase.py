#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittest

class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban.weaver.web.DocumentMill: Toolbar"""
        from luban.content.Toolbar import Toolbar
        document = toolbar = Toolbar()
        toolbar.button(label='button1')
        toolbar.button(label='button2')
        toolbar.spacer()
        toolbar.button(label='button3')

        from luban.weaver.web.Librarian import Librarian
        librarian = Librarian()
        librarian.register('base', ['myproject.css'], ['luban-base.js'])
        
        from luban.weaver.web.DocumentMill import DocumentMill
        mill = DocumentMill(librarian=librarian)

        from luban.weaver.web.content.HtmlDocument import HtmlDocument
        htmldoc = HtmlDocument()
        
        body, jsdoc = mill.render(document, html_target=htmldoc)
        
        from luban.weaver.web.weaver import weave
        texts = weave(htmldoc, javascriptdoc = jsdoc)
        
        filename = 'toolbar-test1.html'
        out = open(filename, 'w')
        print >>out, '\n'.join(texts)
        return
     
    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
