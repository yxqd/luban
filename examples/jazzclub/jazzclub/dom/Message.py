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

class Message(Table):

    name = 'messages'
    
    import dsaw.db
    
    id = dsaw.db.varchar(name='id', length=16)
    id.constraints = 'PRIMARY KEY'
    id.meta['tip'] = "the unique id"

    from User import User
    author = dsaw.db.reference(name='author', table=User)
    subject = dsaw.db.varchar(name='subject', length=256)
    content = dsaw.db.varchar(name='content', length=1024)
    created = dsaw.db.time(name='created')

    from Thread import Thread
    thread = dsaw.db.reference(name='thread', table=Thread)
    

# version
__id__ = "$Id$"

# End of file 
