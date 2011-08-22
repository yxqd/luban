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

'''
test scripts for dealing with luban projects
'''


import unittest, os, shutil

class TestCase(unittest.TestCase):
     
    def test1(self):
        """create-luban-project"""
        default_project = 'helloworld'
        if os.path.exists(default_project):
            shutil.rmtree(default_project)
        cmd = 'create-luban-project.py'
        self.assertEqual(os.system(cmd),0)
        self.assert_(os.path.exists(default_project))

        test_project = 'test'
        if os.path.exists(test_project):
            shutil.rmtree(test_project)
        cmd = 'create-luban-project.py %s' % test_project
        self.assertEqual(os.system(cmd),0)
        self.assert_(os.path.exists(test_project))        
        return


    def test2(self):
        """download-luban-project"""
        project = 'aokuang'
        if os.path.exists(project):
            shutil.rmtree(project)
        cmd = 'download-luban-project.py %s' % project
        self.assertEqual(os.system(cmd), 0)
        self.assert_(os.path.exists(project))
        return


    def test3(self):
        """start-luban-project"""
        project = 'aokuang'
        if os.path.exists(project):
            shutil.rmtree(project)
        cmd = 'download-luban-project.py %s' % project
        self.assertEqual(os.system(cmd), 0)
        self.assert_(os.path.exists(project))

        cmd = 'start-luban-project.py --open-browser=no %s' % project
        self.assertEqual(os.system(cmd), 0)
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
