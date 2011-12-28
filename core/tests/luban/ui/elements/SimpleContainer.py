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


from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


import unittest

class TestCase(unittest.TestCase):

    def test1(self):
        from luban.ui.elements.SimpleContainer import SimpleContainer
        return
    

    def test2(self):
        from luban.ui.elements.SimpleContainer import SimpleContainer
        class F(SimpleContainer):
            s = descriptors.str()
        return
    


def main():
    from luban import journal
    journal.debug('metaclass').active = True
    journal.debug('ui element lookup').active = True
    unittest.main()
    return
    
    
if __name__ == "__main__": main()

    
# version
__id__ = "$Id$"

# End of file 
