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


# End of file 
