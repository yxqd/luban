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
     
    def test(self):
        """luban.weaver.web.weaver"""
        from luban.weaver.web.content.HtmlDocument import HtmlDocument
        document = HtmlDocument()
        body = document.body
        div = body.tag('div')
        for i in range(12):
            div = div.tag('div')
        
        from luban.weaver.web.content.JavaScriptDocument import JavaScriptDocument
        jsdoc = JavaScriptDocument()
        
        from luban.weaver.web.weaver import weave
        texts = weave(document, javascriptdoc = jsdoc)

        print '\n'.join(texts)
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
