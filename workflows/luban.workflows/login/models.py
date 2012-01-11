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

# shows an example implementation of User model

from sqlalchemy import Table, Column, Integer, String, DateTime
import datetime
from ..models import model_registry as reg


def createUser(Base):

    if not Base:
        raise RuntimeError("should define base")
    

    class User(Base):

        __tablename__ = 'users'

        id = Column(Integer, primary_key = True)
        username = Column(String, unique = True) 
        password = Column(String)
        email = Column(String(100), unique = True)
        firstname = Column(String(100))
        lastname = Column(String(100))
        time_created = Column(DateTime, default = datetime.datetime.now)

        pass

    reg.register(User)

    return User


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
