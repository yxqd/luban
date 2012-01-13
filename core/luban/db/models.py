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


# example base class of model
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

# XXX: thinking of use metaclass...
class ModelCollector:

    def __new__(cls, name, bases, attributes, **kwds):
        # the created class
        created = super().__new__(cls, name, bases, attributes, **kwds)
        model_registry.register(created)
        return created


class ModelRegistry:

    def __init__(self):
        self.models = {}
        return
    

    def register(self, cls):
        self.models[cls.__name__] = cls
        return


    def __getattr__(self, name):
        return self.models[name]

model_registry = ModelRegistry()


# method to load all db models in a python sub-package
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
        continue
    return


# End of file 
