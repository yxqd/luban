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

    from .model import Factory as model_factory
    from .actor import Factory as actor_factory
    from .form import Factory as form_factory

    def __init__(self, db, ):
        self.model = self.model_factory()
        
        self.actor_factory.User = model
        self.actor_factory.db = db
        
        self.actor = self.actor_factory()
        return


# End of file 
