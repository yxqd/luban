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


# to extend luban with all element types provided by this package
# one needs to import all the modules that define element classes
# and action classes
modules = [
    'Form',
    'Reboot',
    ]
def importAllModules():
    for name in modules:
        m = __import__(name, fromlist=['.'], globals=globals())
        continue
    return
importAllModules()
del importAllModules

    
# End of file 
