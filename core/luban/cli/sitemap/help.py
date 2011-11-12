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
    from . import public_commands
    print( 'luban sitemap -- sitemap related commands')
    print( 'http://lubanui.org')
    print()
    print('Commands:')
    for cmd in public_commands:
        print('  luban sitemap %s' % cmd)
        continue
    return
    

def parse_cmdline():
    return [], {}

# End of file 

