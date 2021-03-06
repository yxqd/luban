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
    
    from .CreateProjectInFS import Renderer
    Renderer().render(project, outdir)
    
    return
    

def loadProject(path=None):
    if path is None: path = '.'
    import os
    if os.path.isdir(path):
        path = os.path.join(path, 'conf.py')
    try:
        return loadProject_fromConfPy(path)
    except:
        msg = "Failed to load project from %r" % (path,)
        raise RuntimeError(msg)
        

def loadProject_fromConfPy(filename):
    from .ConfigurationLoader import ConfigurationLoader
    loader = ConfigurationLoader()
    return loader.load(filename)


# End of file 

