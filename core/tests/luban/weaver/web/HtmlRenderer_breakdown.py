#!/usr/bin/env python3
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


import luban.ui as lui


import unittest

class TestCase(unittest.TestCase):
     
    def test(self):
        """luban.weaver.web: Frame2HtmlDocument + renderer.render"""
        # luban ui object
        frame = lui.e.frame(title='test frame', name='frame')
        document = frame.document(name='document')
        p = document.paragraph(name='p')
        
        # frame->htmldoc renderer
        from luban.weaver.web.Librarian import Librarian
        librarian = Librarian()
        librarian.register('base', ['myproject.css'], ['luban-base.js'])
        
        from luban.weaver.web.JsonReprRenderer import JsonReprRenderer
        obj2json = JsonReprRenderer()
        from luban.weaver.web.Frame2HtmlDocument import Frame2HtmlDocument
        mill = Frame2HtmlDocument(librarian=librarian, obj2json=obj2json)
        
        # htmldoc
        from luban.weaver.web.content.HtmlDocument import HtmlDocument
        htmldoc = HtmlDocument()
        
        # frame->htmldoc
        body, jsdoc = mill.render(frame, html_target=htmldoc)
        
        # htmldoc -> text
        from luban.weaver.web.renderer import render
        texts = render(htmldoc, javascriptdoc = jsdoc)
        
        #
        filename = 'out-HtmlRenderer-breakdown-test.html'
        out = open(filename, 'w')
        print('\n'.join(texts), file=out)
        
        return
     
    
def main():
    from luban import journal
    # journal.debug('luban.weaver.web').activate()

    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
