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


import luban


import unittest

class TestCase(unittest.TestCase):
     
    def test(self):
        """luban.weaver.web: Frame2HtmlDocument + renderer.render"""
        # luban ui object
        frame = luban.e.frame(title='test frame', name='frame')
        document = frame.document(name='document')
        p = document.paragraph(name='p')
        action = luban.a.establishInterface(frame)
        
        # frame->htmldoc renderer
        from luban.weaver.web import create
        weaver = create()
        text = weaver.weave(action)
        
        #
        filename = 'out-t2.html'
        out = open(filename, 'w')
        out.write(text)
        
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
