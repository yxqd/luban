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


import luban.db.sqlalchemy


from sqlalchemy import Table, Column, Integer, String, DateTime
import datetime
from ..models import model_registry as reg


from ..login.models import createUser

class Factory:

    Base = None

    def __call__(self):
        from ..models import model_registry as reg

        try:
            reg.User
        except KeyError:
            createUser(self.Base)
            
        return
    
factory = Factory()


# End of file 
