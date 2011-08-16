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
    # to register all element types provided by a package
    # one needs to import all the modules that define element classes
    from luban.ui import elements as lue
    
    modules = types
    for name in modules:
        m = __import__(name, fromlist=['.'], globals=globals())
        
        # one could make this element available in the luban.ui.elements
        # namespace if so desired
        setattr(lue, name.lower(), getattr(m, name))
        continue
    return

    
# End of file 
