# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

__doc__ = """ luban.ui.Event
"""


from .AttributeContainer import AttributeContainer
class Event(AttributeContainer):

    # decorators
    

    def __getattr__(self, key):
        from .actions.GetAttr import GetAttr
        return GetAttr(entity=self, name=key)


    def identify(self, inspector):
        return inspector.onEvent(self)



# version
__id__ = "$Id$"

# End of file 
