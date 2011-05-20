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


def usersFromDB(**kwds):
    from UsersFromDB import UsersFromDB
    return UsersFromDB(**kwds)


def painter(**kwds):
    from Painter import Painter
    return Painter(**kwds)


def clerk(**kwds):
    from Clerk import Clerk
    return Clerk(**kwds)


# version
__id__ = "$Id$"

# End of file 
