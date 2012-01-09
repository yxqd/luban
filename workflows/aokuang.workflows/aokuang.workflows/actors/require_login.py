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
This is better and simpler than the "login" example.
It uses the "require" decorator.

http://localhost:22347/require_login
"""

import luban
from ..decorators import authentication_portal


from ..workflows.login import workflow
class Actor(workflow.Actor):

    expose = 1

    @luban.decorators.require(authentication_portal)
    def default(self, **kwds):
        frame = luban.e.frame(title='Welcome')
        frame.document(title='Welcome')
        return frame
    
    pass


# End of file 
