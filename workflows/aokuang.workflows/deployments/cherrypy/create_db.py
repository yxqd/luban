#!/usr/bin/env python3

from sqlalchemy import create_engine
from aokuang_workflows_config import dburi
engine = create_engine(dburi)

# import all workflows
from aokuang.workflows.workflows import importModels
importModels()

from aokuang.workflows.db import Base
Base.metadata.create_all(engine)

from aokuang.workflows.db import models, createSession
session = createSession()

User = models.User
user = User()
user.username = 'linjiao'
import hashlib
user.password = hashlib.md5('1234'.encode()).hexdigest()
session.add(user)
session.commit()
