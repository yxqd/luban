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


# model registry
from luban.workflows.models import model_registry as models

# model base
from ..db import Base as ModelBase

#
workflows = [
    'login',
    ]
def importModels():
    for mod in workflows:
        module = __import__(mod, globals=globals())
        module.Workflow.createModels()
        continue
    return


# End of file 
