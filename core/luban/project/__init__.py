# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


__doc__ = """
"""


def createProjectSkeleton(name, outdir, deployment=None):
    from .Project import Project
    project = Project(name=name)
    
    import os
    projdir = os.path.join(outdir, name)
    if os.path.exists(projdir):
        raise IOError(projdir + " already exists")
    
    from luban.project.CreateProjectInFS import Renderer
    Renderer().render(project, outdir)

    # reload project
    conf = os.path.join(outdir, project.name, 'conf.py')
    project = loadProject(conf)
    
    # create a deployment
    deployment = deployment or 'cherrypy'
    from luban.project.deployment import createDeployment
    path = os.path.join(outdir, project.name, 'deployments')
    createDeployment(deployment, project, path)
    return    
    
    

def loadProject(filename):
    from .ConfigurationLoader import ConfigurationLoader
    loader = ConfigurationLoader()
    return loader.load(filename)


# End of file 

