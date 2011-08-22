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


def democlerk(**kwds):
    from DemoClerk import Clerk
    return Clerk(**kwds)


def usersFromDB(**kwds):
    from UsersFromDB import UsersFromDB
    return UsersFromDB(**kwds)


# version
__id__ = "$Id$"

# End of file 
