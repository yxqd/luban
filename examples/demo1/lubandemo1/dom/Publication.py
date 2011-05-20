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

class Publication(Table):

    name = 'publication'
    
    import pyre.db
    id = pyre.db.varchar(name='id', length=16)
    title = pyre.db.varchar(name='title', length=128)
    abstract = pyre.db.varchar(name='abstract', length=8192)
    journaltitle = pyre.db.varchar(name='journaltitle', length=128)
    

# version
__id__ = "$Id$"

# End of file 
