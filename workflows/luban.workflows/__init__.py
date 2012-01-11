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


"""
example workflows

In this subpackage "luban.workflows", any "public" subpackage
(whose name is without '_' prefix) represents one workflow.

Each subpackage should define one Workflow class that inherits
from .Workflow.Workflow.

See more details about workflow convention in base class
.Workflow.Workflow.

"""


import luban.timber # default implementation of luban workflows depend on timber


# End of file 
