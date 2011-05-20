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


import unittest

class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban._filesystem.Writer"""

        from luban._filesystem.Directory import Directory
        from luban._filesystem.File import File
        from luban._filesystem.SymLink import SymLink
        
        root = Directory('out.Writer_TestCase_test1-root')
        import os
        if os.path.exists(root.name):
            import shutil
            shutil.rmtree(root.name)
            
        root.addEntry(File('a.txt', 'hello'))
        
        subdir1 = Directory('subdir1')
        root.addEntry(subdir1)
        subdir1.addEntry(SymLink('link-to-a.txt', '../a.txt'))

        from luban._filesystem.Writer import Writer
        writer = Writer()
        writer.render(root)
        writer.render(root, overwrite=True)
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
