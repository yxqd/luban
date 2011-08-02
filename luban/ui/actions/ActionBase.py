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



from .AttributeContainer import AttributeContainer, Meta
class ActionBase(AttributeContainer):

    """base class of all actions
    """
    
    abstract = True
    
    def __init__(self, name=None, **kwds):
        AttributeContainer.__init__(self)
        
        self.name = name

        for k, v in kwds.items():
            self.setAttribute(k,v)

        return


# version
__id__ = "$Id$"

# End of file 
