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



def propertySet(name, pattern, **kwds):
    from PropertySet import PropertySet
    return PropertySet(name, pattern, **kwds)


from _frompyre import *
from _validators import *


def date(name, **kwds):
    from Date import Date
    return Date(name, **kwds)


# version
__id__ = "$Id$"

# End of file 
