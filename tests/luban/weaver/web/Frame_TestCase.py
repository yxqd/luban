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


import unittest

class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban.weaver.web.DocumentMill: Frame"""
        import luban.ui.elements as lue
        frame = lue.frame(name='frame')
        document = frame.document(name='document')
        
        from luban.weaver.web.Librarian import Librarian
        librarian = Librarian()
        librarian.register('base', ['myproject.css'], ['luban-base.js'])
        librarian.register('appmenubar', ['appmenubar.css'], ['appmenubar.js'])
        
        from luban.weaver.web.DocumentMill import DocumentMill
        mill = DocumentMill(librarian=librarian)

        from luban.weaver.web.content.HtmlDocument import HtmlDocument
        htmldoc = HtmlDocument()
        
        body, jsdoc = mill.render(frame, html_target=htmldoc)
        
        from luban.weaver.web.weaver import weave
        texts = weave(htmldoc, javascriptdoc = jsdoc)
        
        filename = 'Frame-test1.html'
        out = open(filename, 'w')
        print('\n'.join(texts), file=out)
        return
     
    
def main():
    import journal
    # journal.debug('luban.weaver.web').activate()
    
    unittest.main()
    return

    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
