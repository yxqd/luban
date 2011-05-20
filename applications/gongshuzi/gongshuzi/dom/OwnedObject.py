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


from User import User


from WithID import WithID

class OwnedObject(WithID):

    import dsaw.db
    
    creator = dsaw.db.reference(name='creator', table=User)
    time_created = dsaw.db.time(name='time_created')

    

# version
__id__ = "$Id$"

# End of file 
