#!/usr/bin/env python3
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


types = [
    'Form',
    ]
def registerAllElements():
    from luban.ui import elements as lue
    
    modules = types
    for name in modules:
        m = __import__(name, fromlist=['.'], globals=globals())
        setattr(lue, name.lower(), getattr(m, name))
        continue
    return

    
# End of file 
