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


import os

def run(*args, **kwds):
    from . import commands
    print( 'luban - a UI "language"')
    print( 'http://lubanui.org')
    print()
    print('Basic commands:')
    for cmd in commands:
        print('  luban %s' % cmd)
        continue
    return
    

def parse_cmdline():
    return [], {}

# End of file 

