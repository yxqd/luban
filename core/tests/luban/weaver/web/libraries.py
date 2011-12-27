#!/usr/bin/env python3
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
     
    def test1(self):
        """luban.weaver.web.Library"""
        import luban
        luban.debug = 1
        from luban.weaver.web.libraries import default
        return
     
    
def main():
    from luban import journal
    # journal.debug('luban.weaver.web').activate()
    
    unittest.main()
    return

    
if __name__ == "__main__":
    main()
    
# End of file 
