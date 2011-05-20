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
        """luban.weaver.web.DocumentMill: AppMenuBar"""
        from luban.content.AppMenuBar import AppMenuBar
        menubar = AppMenuBar()
        document = menubar

        menu1 = menubar.menu(label='menu1')
        menu1.item(label='item11')

        item2 = menubar.item(label='item2')

        menu3 = menubar.menu(label='menu3')
        menu3.item(label='item31')
        menu32 = menu3.menu(label='menu32')

        item321 = menu32.item(label='item321')
        item322 = menu32.item(label='item322')
        menu322 = menu32.menu(label='menu322')
        item3221 = menu322.item(label='item3221')

        from luban.weaver.web.Librarian import Librarian
        librarian = Librarian()
        librarian.register('base', ['myproject.css'], ['luban-base.js'])
        librarian.register('appmenubar', ['appmenubar.css'], ['appmenubar.js'])
        
        from luban.weaver.web.DocumentMill import DocumentMill
        mill = DocumentMill(librarian=librarian)

        from luban.weaver.web.content.HtmlDocument import HtmlDocument
        htmldoc = HtmlDocument()
        
        body, jsdoc = mill.render(document, html_target=htmldoc)
        
        from luban.weaver.web.weaver import weave
        texts = weave(htmldoc, javascriptdoc = jsdoc)
        
        filename = 'AppMenuBar-test1.html'
        out = open(filename, 'w')
        print >>out, '\n'.join(texts)
        return
     
    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
    journal.debug('luban.weaver.web').activate()
    
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
