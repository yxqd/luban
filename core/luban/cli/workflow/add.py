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


import os, sys, time, shutil


def run(workflow, project=None):
    # check if the workflow exists
    mod = 'luban.workflows.%s' % workflow
    try:
        __import__(mod, locals=locals(), globals=globals())
    except ImportError:
        print ("***workflow %r does not exist.\n" % workflow)
        print_available_workflows()
        return
    
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
    import aokuang.workflows as awpkg
    awpkgpath = os.path.dirname(awpkg.__file__)
    actorsrc = os.path.join(awpkgpath, 'actors', workflow+'.py')
    workflowsrc = os.path.join(awpkgpath, 'workflows', workflow+'.py')
    if not os.path.exists(actorsrc) or not os.path.exists(workflowsrc):
        print ("workflow template was not installed correctly.")
        print ("missing %s or %s" % (actorsrc, workflowsrc))
        return
        
    shutil.copy(actorsrc, actor_file)
    print ("created %s" % actor_file)
    shutil.copy(workflowsrc, workflow_file)
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
        msg = "incorrect number of arguments.\n\n"
        msg += available_workflows_str()
        parser.error(msg)

    args, kwds = args[2:], vars(options)
    return args, kwds



def print_available_workflows():
    print(available_workflows_str())


def available_workflows_str():
    s = ["available workflows: "]
    workflows = collect_workflows()
    for wf in workflows:
        s.append(" - %s: %s" % (wf.name, wf.__doc__.strip()))
        continue
    return '\n'.join(s)


def collect_workflows():
    prefix = 'luban.workflows.'
    import luban.workflows as pkg
    workflows = []
    import pkgutil
    for mod_loader, name, ispkg in pkgutil.iter_modules(pkg.__path__):
        # skip over "private" stuff
        if name.startswith('_'): continue
        # and modules
        if not ispkg: continue
        #
        pkgname = prefix + name
        # get workflow class
        __import__(pkgname, globals=globals(), locals=locals(), level=-1)
        workflow_mod = sys.modules[pkgname]
        try:
            wf = workflow_mod.Workflow
        except AttributeError:
            msg = "module %r does not define Workflow class" % (workflow_mod,)
            raise NotImplementedError(msg)
        # 
        wf.name = name
        workflows.append(wf)
        continue
    return workflows

# End of file 

