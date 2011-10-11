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
    

    def __init__(self, name):
        self.name = name
        # XXX
        # these names are differnt from those of class variables
        # because the object variables could be changed in the future to
        # absolute paths
        self.pytree_container = self.python_in_project
        self.actors_pkg = name + self.actors_in_python
        self.web_static = self.web_static_in_project
        return

    def identify(self, inspector):
        return inspector.onProject(self)


# End of file 

