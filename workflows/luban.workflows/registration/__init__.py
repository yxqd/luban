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


# registration workflow
from ..Workflow import Workflow as base
class Workflow(base):

    """
    user registration workflow 
    """

    from .models import factory as models_factory
    from .actor import factory as actor_factory
    from .visuals import factory as visual_factory

    def _configureActorFactory(self): return
    def _configureVisualFactory(self): return


# End of file 
