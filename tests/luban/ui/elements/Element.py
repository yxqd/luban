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


from luban.ui.elements.Element import Element


import unittest
class TestCase(unittest.TestCase):

    def test0(self):
        "Element: ctor"
        e = Element()
        return
     
    
    def test1(self):
        "Element: ctor -- attrs"
        from luban.ui.elements.Element import Element
        try:
            e = Element(a=3)
        except AttributeError:
            pass
        else:
            m = "should raise AttributeError"
            raise Exception(m)

        #
        class T(Element):
            a = descriptors.str()
        t = T(a=3)
        return


    def test2(self):
        "Element: getCtorDocStr"
        class T2(Element):
            a = descriptors.str()

        docstr = T2.getCtorDocStr()
        # print(docstr)
        return
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
