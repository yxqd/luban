#!/usr/bin/env python3

# XXX this should not be necessary XXX
import luban.timber

from sqlalchemy import create_engine
from aokuang_workflows_config import dburi
engine = create_engine(dburi)

# import all workflows
from aokuang.workflows.workflows import importAll
importAll()

from aokuang.workflows.db import Base
Base.metadata.create_all(engine)

