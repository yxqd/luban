#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao  Lin
#                      California Institute of Technology
#                      (C) 2005-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from .ActionBase import ActionBase, Meta
class Action(ActionBase):

    """base class of usual actions (all actions except NoAction)
    """

    # decorations
    abstract = True
    
    # attributes
    
    # XXX: this needs more thought. probably it is better to
    # XXX: put this into those actions that really need 'onfinish'.
    # onfinish = descriptors.eventhandler()
    # onfinish.experimental = True
    # onfinish.tip = 'A callback action that will be performed when the current action is finished'
    

# version
__id__ = "$Id$"

# End of file 
