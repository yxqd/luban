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


from gongshuzi.dom.ProjectSettings import ProjectSettings
from gongshuzi.utils.uniquelist import uniquelist


def getAllPortsUsedExceptMine(db, me):
    all = db.fetchall(ProjectSettings)
    ports = [s.port for s in all if s.id != me.id]
    return uniquelist(ports)

def findUniquePort(db, me):
    ports = getAllPortsUsedExceptMine(db, me)
    if not ports: return lowest_port
    port = max(ports)+1
    if port>58000: raise RuntimeError, 'cannot find a valid port number'
    return port
    

lowest_port = 8500

# version
__id__ = "$Id$"

# End of file 
