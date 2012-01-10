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
from ..Workflow import Workflow as base
class Workflow(base):

    """
    user login workflow
    """

    from .models import factory as models_factory
    from .actor import factory as actor_factory
    from .visuals import factory as visual_factory

    def _configureActorFactory(self): return
    def _configureVisualFactory(self): return


# portal requirement decorator
import luban
def check_token(*args, **kwds):
    token = kwds.get('token')
    token2 = luban.session.get('token')
    # the request must have a token with it, and it must match the saved token
    return not token or not token2 or token != token2

class authentication_frame_factory:

    form_factory = None # override this

    def __call__(self, context):
        form_factory = self.form_factory
        if form_factory is None:
            form_factory = Workflow().visuals.form
            
        frame = luban.e.frame(title='authentication')
        form = form_factory(context=context)
        frame.append(form)
        return frame
authentication_frame = authentication_frame_factory()
authentication_portal = luban.decorators.PortalRequirement()
authentication_portal.check_requirement = check_token
authentication_portal.fullfill_requirement = authentication_frame


# End of file 
