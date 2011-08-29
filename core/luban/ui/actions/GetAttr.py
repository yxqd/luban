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
generic action of obtaining attribute of an object
"""

from .ActionBase import ActionBase
class GetAttr(ActionBase):

    # decorations
    # .. this is a real luban type
    abstract = False


    # attributes
    entity = descriptors.object(dynamic=False) # entity the attribute is about
    name = descriptors.str() # name of the attribute


    def identify(self, inspector):
        return inspector.onGetAttr(self)
    

    pass # end of GetAttr


# version
__id__ = "$Id$"

# End of file 
