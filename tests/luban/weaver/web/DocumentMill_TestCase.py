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
        """luban.weaver.web.DocumentMill: simplest document"""
        from luban.content.Document import Document
        document = Document()

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
        
        filename = 'DocumentMill-test1.html'
        out = open(filename, 'w')
        print >>out, '\n'.join(texts)
        return
     
    
    def test2(self):
        """luban.weaver.web.DocumentMill: created by hand"""
        from luban.content.Document import Document
        document = Document()
        splitter = document.splitter()
        left = splitter.section()
        right = splitter.section()

        p = left.paragraph()
        p.text = ['This is the left side']

        form = right.document().form()
        t = form.text(label='text file', value='test')
        ta = form.textarea(label='text area', value='a\nb\nc\n')
        entries=[('1', 'a'), ('2', 'b')]
        s = form.selector(label='selector', entries=entries, selection='2')
        
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

        filename = 'DocumentMill-test2.html'
        out = open(filename, 'w')
        print >>out, '\n'.join(texts)
        return
     
    
    def test3(self):
        """luban.weaver.web.DocumentMill: page created by hand"""
        from luban.content.Page import Page
        page = Page(title='test page')
        document = page.document()
        splitter = document.splitter()
        left = splitter.section()
        right = splitter.section()

        p = left.paragraph()
        p.text = ['This is the left side']

        form = right.document().form()
        t = form.text(label='text file', value='test')
        ta = form.textarea(label='text area', value='a\nb\nc\n')
        entries=[('1', 'a'), ('2', 'b')]
        s = form.selector(label='selector', entries=entries, selection='2')
        
        from luban.weaver.web.Librarian import Librarian
        librarian = Librarian()
        librarian.register('base', ['myproject.css'], ['luban-base.js'])
        
        from luban.weaver.web.DocumentMill import DocumentMill
        mill = DocumentMill(librarian=librarian)

        from luban.weaver.web.content.HtmlDocument import HtmlDocument
        htmldoc = HtmlDocument()
        
        body, jsdoc = mill.render(page, html_target=htmldoc)
        
        from luban.weaver.web.weaver import weave
        texts = weave(htmldoc, javascriptdoc = jsdoc)

        filename = 'DocumentMill-test3.html'
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
