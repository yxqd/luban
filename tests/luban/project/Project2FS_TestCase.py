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
        """luban.project.Project2FS"""

        outdir = 'out-Project2FS_TestCase-test1'
        
        from luban.project.Project import Project
        project = Project()
        project.name='myproject'

        from luban.project.Actor import Actor
        actor = Actor()
        actor.actorname='subdir/test'
        actor.content=['# ...']
        project.actors.append(actor)

        import os
        if os.path.exists(outdir):
            import shutil
            shutil.rmtree(outdir)

        from luban.project.Project2FS import Project2FS
        Project2FS().render(project, outdir)
        
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
