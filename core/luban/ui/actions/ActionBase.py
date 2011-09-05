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

    # decorations
    abstract = True

    # don't override this
    lubanaction = descriptors.bool(default=True)


# version
__id__ = "$Id$"

# End of file 
