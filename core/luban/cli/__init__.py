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
    code = 'from . import %s' % action
    exec(code)
    mod = locals()[action]
    return mod.run(*args, **opts)


def main():
    import sys
    action = sys.argv[1]
    name = sys.argv[2]
    run(action, name)
    return


# End of file 

