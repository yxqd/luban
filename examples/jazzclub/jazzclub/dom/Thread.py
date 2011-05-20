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


from Table import Table

class Thread(Table):

    name = 'threads'
    
    import dsaw.db
    
    id = dsaw.db.varchar(name='id', length=16)
    id.constraints = 'PRIMARY KEY'
    id.meta['tip'] = "the unique id"
    
    from User import User
    author = dsaw.db.reference(name='author', table=User)
    
    subject = dsaw.db.varchar(name='subject', length=256)
    created = dsaw.db.time(name='created')
    

# version
__id__ = "$Id$"

# End of file 
