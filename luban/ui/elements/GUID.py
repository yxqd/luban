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


# overload this method to provide custom way of generating global
# unique id. 
# if that is done, it means that it would be total mess if two different
# projects are run from the same python session.
# But I cannot really imagine that two projects 
# will be running in the same session right now. 
def GUID(obj):
    return id(obj)


# version
__id__ = "$Id$"

# End of file 
