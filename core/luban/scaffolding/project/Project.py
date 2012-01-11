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


class Project:
    
    name = None
    
    root = None # absolute path of this project

    web_static_in_project = 'web/static' # path of directory for static web files relative to root

    python_in_project = 'python' # path of python src tree container dir relative to root
    
    actors_in_python = '.actors' # name of the actors python subpackage in the project python namespace
    workflows_in_python = '.workflows' # name of the workflows python subpackage in the project python namespace

    deployment = 'cherrypy' # deployment method
    extensions = ['luban.timber', 'luban.workflows'] # luban extensions used

    # server
    port = 8080 # port number
    

    def __init__(
        self, name,
        pytree_container = None,
        actors_pkg = None,
        workflows_pkg = None,
        web_static = None,
        deployment = None,
        extensions = None,
        port = None,
        ):
        self.name = name
        # XXX
        # these names are differnt from those of class variables
        # because the object variables could be changed in the future to
        # absolute paths
        self.pytree_container = pytree_container or self.python_in_project
        self.actors_pkg = actors_pkg or name + self.actors_in_python
        self.workflows_pkg = workflows_pkg or name + self.workflows_in_python
        self.web_static = web_static or self.web_static_in_project
        # 
        self.deployment = deployment or self.deployment
        self.extensions = extensions or self.extensions
        self.port = port or self.port
        return


    def getDeploymentPath(self):
        return os.path.join(self.root, 'deployments', self.deployment)


    def getAppConfigPy(self):
        dep = self.getDeploymentPath()
        return os.path.join(dep, 'luban_app_config.py')


    def getPyTreeRoot(self):
        return os.path.join(self.root, self.pytree_container)


    def setPythonPath(self):
        mypytreeroot = self.getPyTreeRoot()
        import sys
        if mypytreeroot not in sys.path:
            sys.path.insert(0, mypytreeroot)
        if '.' not in sys.path:
            sys.path.insert(0, '.')
        return
    

    def identify(self, inspector):
        return inspector.onProject(self)



# these are relative paths in the configuration 
relpaths = [
    'pytree_container',
    'web_static',
    ]


import os

# End of file 

