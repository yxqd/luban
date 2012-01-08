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

session = None

def getSession():
    global session
    if session: return session
    from .sqlalchemy_cherrypy_tool import session as s
    session = s
    return session


def uuid():
    import uuid
    return str(uuid.uuid4())


def createSession(create_metadata=True, engine=None):
    if engine is None:
        engine = createEngine()
    
    if create_metadata:
        Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    global session
    session = Session()
    return session


def createEngine():
    from sqlalchemy import create_engine
    from aokuang_workflows_config import dburi
    engine = create_engine(dburi)
    return engine


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from ..workflows import models

__all__ = ['createSession', 'models']


# End of file 
