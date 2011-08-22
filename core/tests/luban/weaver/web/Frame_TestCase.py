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
        import luban.ui as lui
        frame = lui.e.frame(name='frame')
        document = frame.document(name='document')
        
        from luban.weaver.web import create
        weaver = create(htmlbase="http://my.url.com/")
        text = weaver.weave(frame)
        
        filename = 'Frame-test1.html'
        out = open(filename, 'w')
        print(text, file=out)
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
