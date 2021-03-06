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
        """luban.scaffolding.project.deployment.cherrypy"""

        outdir = 'deployments'
        
        import os
        os.chdir('testproj')
        
        #
        filename = "conf.py"
        from luban.scaffolding.project import loadProject
        project = loadProject(filename)

        #
        from luban.scaffolding.project.deployment import createDeployment
        createDeployment('cherrypy', project, outdir)
        
        return
     
    
def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
