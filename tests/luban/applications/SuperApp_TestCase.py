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


import unittest, os

class TestCase(unittest.TestCase):

    pass


def addTestForCommand(index, cmd):
    def _(self):
        self.assertEqual(os.system(cmd), 0)
        return
    _.__doc__ = """luban.applications.SuperApp: %s""" % cmd
    setattr(TestCase, 'test%s' % index, _)
     

cmds = [
    'python dummyapp.py',
    'python dummyapp.py --config=a',
    'python dummyapp.py --greeting=aloha',
    'python dummyapp.py --config=a --- --greeting=aloha',
    'python dummyapp.py --help-properties ---',
    'python dummyapp.py --- --help-properties',
    'python dummyapp.py --config=a --help-properties ---',
    'python dummyapp.py --- --greeting=aloha --help-properties',
    ]

for i, cmd in enumerate(cmds):
    addTestForCommand(i, cmd)
    continue
     
    
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
