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


import unittest

class TestCase(unittest.TestCase):
     
    def test1(self):
        """luban.scaffolding.project.createProjectSkeleton"""

        outdir = 'out-createProjectSkeleton'
        
        import os
        if os.path.exists(outdir):
            import shutil
            shutil.rmtree(outdir)

        from luban.scaffolding.project import createProjectSkeleton
        createProjectSkeleton('myproject', outdir)
        return
     
    
def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
