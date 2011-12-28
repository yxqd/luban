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


import luban.ui
from luban.weaver.Dict2Object import Dict2Object


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        d = {'type': 'document', 'title': 'hello'}
        doc = Dict2Object().render(d)
        # print(doc)
        return
    

    def test2(self):
        d = {'type': 'document', 'title': 'hello', 'contents':
                 [{'type': 'document', 'title': 'subdoc'}]}
        doc = Dict2Object().render(d)
        # print (doc)
        # print(doc.contents)
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
