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


from . import ModelBase
from luban.workflows.login import Workflow
Workflow.models_factory.Base = ModelBase

@Workflow.factory
def workflow():
    workflow = Workflow()
    # overload decorators
    from luban.workflows.login import authentication_portal
    authentication_portal.fullfill_requirement.form_factory = workflow.visuals.form
    return workflow


# End of file 
