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


def run(action, *args, **opts):
    mod = importActionHandler(action)
    return mod.run(*args, **opts)


def importActionHandler(action):
    code = 'from . import %s' % action
    exec(code)
    mod = locals()[action]
    return mod


def parse_cmdline():
    import sys
    if len(sys.argv) == 2:
        action = 'help'
    else:
        action = sys.argv[2]

    if action in ['-h', '--help']:
        action = 'help'

    if action not in commands:
        print ()
        print ("Invalid command: %s" % action)
        action = 'help'
    
    mod = importActionHandler(action)
    args, kwds = mod.parse_cmdline()
    return args, kwds


public_commands = [
    'help',
    'xml',
    'snapshots',
    ]

hidden_commands = [
    ]


commands = public_commands + hidden_commands


# End of file 

