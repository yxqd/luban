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


"""
add a workflow
"""


import os, time, shutil


def run(workflow, project=None):
    project = project or '.'
    project = os.path.abspath(project)
    print ("adding workflow %r to luban project %r" % (workflow, project))

    # load the project
    from luban.scaffolding.project import loadProject
    path = project
    conf = os.path.join(path, 'conf.py')
    project = loadProject(conf)
    
    # see if files already exist
    actor_file = os.path.join(path, project.pytree_container, project.actors_pkg.replace('.', '/'), workflow+'.py')
    workflow_file = os.path.join(path, project.pytree_container, project.workflows_pkg.replace('.', '/'), workflow+'.py')
    if os.path.exists(actor_file) or os.path.exists(workflow_file):
        print("Cannot create workflow template because %s and/or %s already exist" % (actor_file, workflow_file))
        return
    
    # actor
    mod = "aokuang.workflows.actors.%s" % (workflow,)
    try:
        mod = __import__(mod, fromlist = [''])
    except ImportError:
        print("Cannot import workflow template from %s" % mod)
        return
    else:
        shutil.copy(mod.__file__, actor_file)
        print ("created %s" % actor_file)
    
    # workflow
    mod = "aokuang.workflows.workflows.%s" % (workflow,)
    try:
        mod = __import__(mod, fromlist = [''])
    except ImportError:
        print("Cannot import workflow template from %s" % mod)
        return
    else:
        shutil.copy(mod.__file__, workflow_file)
        print ("created %s" % workflow_file)
    
    return


def parse_cmdline():
    import optparse
    usage = "usage: %prog workflow add <workflow> [options]"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    # NOTE:
    # all options should have default None
    parser.add_option(
        '-p', '--project', 
        dest='project', default=None, help='path to the luban project')

    #
    options, args = parser.parse_args()
    if len(args) != 3:
        parser.error("incorrect number of arguments")

    args, kwds = args[2:], vars(options)
    return args, kwds


# End of file 

