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
command line interface
"""


def run(action, *args, **opts):
    mod = importActionHandler(action)
    return mod.run(*args, **opts)


def importActionHandler(action):
    code = 'from . import %s' % action
    exec(code)
    mod = locals()[action]
    return mod


def main():
    import sys
    if len(sys.argv) <= 1:
        action = 'help'
    else:
        action = sys.argv[1]

    if action in ['-h', '--help']:
        action = 'help'

    if action not in commands:
        print ()
        print ("Invalid command: %s" % action)
        action = 'help'
    
    mod = importActionHandler(action)
    args, kwds = mod.parse_cmdline()
    
    mod.run(*args, **kwds)
    return


public_commands = [
    'help',
    'create',
    'deploy',
    'start',
    'stop',
    'creatext',
    'sitemap',
    'workflow',
    'db',
    'paths',
    ]

hidden_commands = [
    'tail',
    ]


commands = public_commands + hidden_commands

# End of file 

