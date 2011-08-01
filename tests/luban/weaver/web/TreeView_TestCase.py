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
        """luban.weaver.web.DocumentMill: TreeView"""
        from luban.content.TreeView import TreeView
        treeview = TreeView()
        document = treeview

        root = treeview.setRoot(label='root')
        
        branch1 = root.branch(label='branch1')
        branch1.leaf(label='leaf11')

        leaf2 = root.leaf(label='leaf2')

        branch3 = root.branch(label='branch3')
        branch3.leaf(label='leaf31')
        branch32 = branch3.branch(label='branch32')

        leaf321 = branch32.leaf(label='leaf321')
        leaf322 = branch32.leaf(label='leaf322')
        branch322 = branch32.branch(label='branch322')
        leaf3221 = branch322.leaf(label='leaf3221')

        from luban.weaver.web.Librarian import Librarian
        librarian = Librarian()
        librarian.register('base', ['myproject.css'], ['luban-base.js'])
        librarian.register('treeview', ['treeview.css'], ['treeview.js'])
        
        from luban.weaver.web.DocumentMill import DocumentMill
        mill = DocumentMill(librarian=librarian)

        from luban.weaver.web.content.HtmlDocument import HtmlDocument
        htmldoc = HtmlDocument()
        
        body, jsdoc = mill.render(document, html_target=htmldoc)
        
        from luban.weaver.web.weaver import weave
        texts = weave(htmldoc, javascriptdoc = jsdoc)
        
        filename = 'TreeView-test1.html'
        out = open(filename, 'w')
        print('\n'.join(texts), file=out)
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
