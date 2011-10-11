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
# name of the project
name = %(name)r

# the container directory of python tree
pytree_container = %(pytree_container)r

# the name of the python (sub)package containing actors
actors_pkg = %(actors_pkg)r

# path to the "static" directory for web presentation
web_static = %(web_static)r

"""

def create(project):
    return template % project.__dict__


# End of file 

