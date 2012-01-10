#!/usr/bin/env python3

from sqlalchemy import create_engine
import luban.db.sqlalchemy, luban
engine = create_engine(luban.app_config.db.uri)

# import all workflows
# from aokuang.workflows.workflows import importModels
# importModels()
from luban.workflows.models import loadModels
import aokuang.workflows.workflows
loadModels(aokuang.workflows.workflows)

from luban.db.sqlalchemy import Base
Base.metadata.create_all(engine)

from luban.db.sqlalchemy import models, createSession
session = createSession()

User = models.User
user = User()
user.username = 'john'
import hashlib
user.password = hashlib.md5('1234'.encode()).hexdigest()
session.add(user)
session.commit()
