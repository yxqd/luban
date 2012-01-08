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


# login workflow
class Workflow:

    from .models import factory as models_factory
    from .actor import factory as actor_factory
    from .form import factory as form_factory
    
    def __init__(self):
        # create models
        self.models_factory()

        #
        from ..models import model_registry as reg
        self.actor_factory.User = reg.User
        self.actor = self.actor_factory()
        
        return


# End of file 
