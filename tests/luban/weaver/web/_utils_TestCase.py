#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittest

class TestCase(unittest.TestCase):


    def test0(self):
        """luban.weaver.web._utils: jsonFindProblematicElement"""
        from luban.weaver.web._utils import jsonFindProblematicElements
        d = {'a': [1,2, jsonFindProblematicElements], 'b': object}

        r = jsonFindProblematicElements(d)
        self.assert_(jsonFindProblematicElements in r)
        self.assert_(object in r)
        return
    
     
    def test1(self):
        """luban.weaver.web._utils: jsonEncode"""
        from luban.weaver.web._utils import jsonEncode
        d = {'a': [1,2,]}        
        s = jsonEncode(d)

        d = {'a': jsonEncode}
        self.assertRaises(RuntimeError, jsonEncode, d)
        try:
            jsonEncode(d)
        except Exception, msg:
            print msg
        return
     
    
    def test2(self):
        """luban.weaver.web._utils: jsonDecode"""
        from luban.weaver.web._utils import jsonDecode, jsonEncode
        d = {'a': [1,2,]}        
        s = jsonEncode(d)
        d1 = jsonDecode(s)
        self.assertEqual(d, d1)

        s = 'abc, d'
        self.assertRaises(RuntimeError, jsonDecode, s)
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
