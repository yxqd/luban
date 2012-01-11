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


from luban.db.models import *


# method to load all db models of workflows in a python sub-package
def loadModels(subpkg):
    # the implementation just import all sub modules in the sub-pkg
    # recursively
    path = subpkg.__path__
    import os
    import pkgutil
    prefix = subpkg.__name__ + '.'
    for loader, module_name, is_pkg in pkgutil.walk_packages(path, prefix):
        found = loader.find_module(module_name)
        if not found:
            print ("%s not found" % module_name)
        else:
            mod = found.load_module(module_name)
            mod.workflow()
        continue
    return


# End of file 
