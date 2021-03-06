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
        """luban.scaffolding.project.CreateProjectInFS"""

        outdir = 'out-CreateProjectInFS_TestCase-test1'
        
        from luban.scaffolding.project.Project import Project
        project = Project(name='myproject')

        import os
        if os.path.exists(outdir):
            import shutil
            shutil.rmtree(outdir)

        from luban.scaffolding.project.CreateProjectInFS import Renderer
        Renderer().render(project, outdir)
        return
     
    
def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
