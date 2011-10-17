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

"""
validators are used to decorate descriptors. for example::

 >>> descriptor.validator = validators.choice([1,2])
 >>> descriptor.validator = validators.notnull

"""

def choice(items):
    def _(v):
        if v in items: return
        m = "%s not in %s" % (v, items)
        raise ValueError(m)
    return _


# version
__id__ = "$Id$"

# End of file 
