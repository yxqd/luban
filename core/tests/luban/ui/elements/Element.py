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

        # help(T2.__init__) # should show a good doc string same as "docstr" above
        return
    

    def test3(self):
        name = "e1"
        
        e1 = Element(name=name, id='e1')
        self.assertEqual(e1.name, name)
        
        attrs = list(e1.iterAttributes())

        self.assertEqual(e1.id, 'e1')
        self.assertRaises(ValueError, setattr, e1, 'id', "a.b")
        return


    def test4(self):
        name = "e1"
        Class = "a b c"
        e1 = Element(name=name, Class=Class)
        self.assertEqual(e1.Class, ["a", "b", "c"])

        e1.addClass('d')
        self.assertEqual(e1.Class, ["a", "b", "c", "d"])
        
        return
     

    def test5(self):
        from luban.ui.actions import load
        verify = load(actor="login", routine="verify")
        e1 = Element(onclick=verify)
        self.assertEqual(e1.onclick, verify)
        return
     
    
if __name__ == "__main__": unittest.main()

    
# version
__id__ = "$Id$"

# End of file 
