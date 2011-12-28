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
        
        from luban.weaver.web.renderer import render
        texts = render(document, javascriptdoc = jsdoc)

        # print('\n'.join(texts))
        return
     
    
def main():
    import unittest
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# End of file 
