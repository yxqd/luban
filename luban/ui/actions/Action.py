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
    
    abstract = True
    
    onfinish = descriptors.action()
    onfinish.experimental = True
    onfinish.tip = 'A callback action that will be performed when the current action is finished'
    

    def __init__(self, **kwds):
        super().__init__()
        
        for k, v in kwds.items():
            self.setAttribute(k,v)

        return


# version
__id__ = "$Id$"

# End of file 
