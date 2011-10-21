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
script dealing with sitemap
"""


import os, time


def run(project=None, urlbase=None):
    path = project or '.'
    if not os.path.exists(path):
        raise IOError("%r does not exist" % path)

    urlbase = urlbase or 'http://example.com'

    # load project
    from luban.scaffolding.project import loadProject
    conf = os.path.join(path, 'conf.py')
    if not os.path.exists(conf):
        raise IOError("luban project configuration file %s does not exist" % conf)
    project = loadProject(conf)

    # add project pytree to python path
    pytree_container = os.path.join(path, project.pytree_container)
    import sys
    if pytree_container not in sys.path:
        sys.path.insert(0, pytree_container)
    
    # get sitemap
    name = project.name
    mod = __import__("%s.sitemap"%name, fromlist=[''])
    
    # create sitemap.xml
    urls = mod.urls
    xmlout = os.path.join(path, project.web_static, 'sitemap.xml')
    from luban.utils.sitemap import create
    create(urlbase, urls, xmlout)
    print ("created sitemap at %s" % xmlout)
    return


def parse_cmdline():
    import optparse
    usage = "usage: %prog sitemap xml [options]"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    # NOTE:
    # all options should have default None
    parser.add_option(
        '-p', '--project', 
        dest='project', default=None, help='path to the luban project')

    parser.add_option(
        '-b', '--urlbase',
        dest = 'urlbase', default=None, help='url base of the web app')

    #
    options, args = parser.parse_args()
    if len(args) > 2:
        parser.error("too many arguments")

    args, kwds = [], vars(options)
    return args, kwds


# End of file 

