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


import luban.ui as lu


import unittest
class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban.weaver.Object2Dict: simplest document"""
        document = lu.e.document(name='document')
        from luban.weaver.Object2Dict import Object2Dict
        o2d = Object2Dict()
        d = o2d.convert(document)
        # print (d)
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
