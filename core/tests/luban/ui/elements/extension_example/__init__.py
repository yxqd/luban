#!/usr/bin/env python
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
types = [
    'Form',
    ]
def importAllElements():
    for name in types:
        m = __import__(name, fromlist=['.'], globals=globals())
        continue
    return
importAllElements()
del importAllElements

    
# End of file 
