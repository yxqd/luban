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


# replace an element with a new element



from luban.ui.actions.ElementActionBase import ElementActionBase as base
class ReplaceElement(base):

    # decorations
    # .. name of action factory method
    factory_method = 'replaceBy'

    # attributes
    newelement = descriptors.object()

    def identify(self, inspector):
        return inspector.onReplaceElement(self)
    

# version
__id__ = "$Id$"

# End of file 

