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
        return

    def identify(self, inspector):
        return inspector.onProject(self)


# End of file 

