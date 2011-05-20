# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# pyre app at this moment takes care of type coersion and validating
# automatically when configuration is loaded.
# This is not desired in ui application.
# In UI app, we need to be able to allow developer to decide
# at what time to apply the coersion and validation.
# Here we just turn off the coersion and validation by setting
# aside the validator and _cast method


from PropertyInterface import PropertyInterface


def _delayedValidationType(propertytype):
    class newtype(PropertyInterface, propertytype):
        pass
    return newtype


types = [
    'Bool', 
    'Float',
    'Integer',
    'String',
    'Array',
    'Dimensional',
    'List',
    'Slice',
    ]
pkg = 'pyre.inventory.properties'
def _importType(name):
    return getattr(__import__('%s.%s' % (pkg, name), {}, {}, ['']), name)
types = [ _importType(type) for type in types]


__all__ = ['PropertyInterface']
for t in types:
    newt = _delayedValidationType(t)
    name = t.__name__.lower()
    exec '%s = newt' % (name,)
    __all__.append(name)
    continue

str = string
__all__.append('str')

int = integer
__all__.append('int')

# from pyre.inventory import bool
# __all__.append('bool')


# version
__id__ = "$Id$"

# End of file 
