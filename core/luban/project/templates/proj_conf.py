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


template = """
name = %(name)r
python_tree_container_directory = %(pytree_container)r
actors_pkg = %(actors_pkg)r
web_static_directory = %(web_static)r

"""

def create(project):
    name = project.name
    pytree_container = project.python_in_project
    actors_pkg = name + project.actors_in_python
    web_static = project.web_static_in_project
    return template % locals()


# End of file 

