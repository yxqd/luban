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


def createDeployment(name, project, path, overwrite=True):
    code = 'from . import %s' % name
    exec(code)
    mod = locals()[name]
    tree = mod.createTree(project)

    from luban._filesystem.Writer import Writer
    writer = Writer()
    writer.render(tree, path, overwrite=overwrite)
    
    import os
    deployment_root = os.path.join(path, tree.name)
    mod.populateWebStatic(deployment_root, project)
    return

# End of file 

