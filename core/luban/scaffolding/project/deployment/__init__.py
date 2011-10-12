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
scaffolding for deployment
"""


def createDeployment(name, project, path, onconflict = 'skip'):
    """create deployment directory
    
    name: name of the deployment
    project: luban project this is about
    path: directory in which the deployment directory will be established
    onconflict: strategy when there is conflict when trying to create directories, files, etc
    """
    code = 'from . import %s' % name
    exec(code)
    mod = locals()[name]
    tree = mod.createTree(project)

    from luban._filesystem.Writer import Writer
    writer = Writer()
    writer.render(tree, path, onconflict=onconflict)
    
    import os
    deployment_root = os.path.join(path, tree.name)
    mod.populateWebStatic(deployment_root, project)
    return deployment_root


# End of file 

