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


from sqlalchemy import Table, Column, Integer, String, DateTime


def createUser(Base):

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

    return User


class Factory:

    Base = object

    def __call__(self):
        return createUser(self.Base)


# End of file 
