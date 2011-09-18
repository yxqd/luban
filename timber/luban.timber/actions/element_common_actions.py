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


from luban.ui.actions.ElementActionBase import ElementActionBase as base


class ReplaceElement(base):

    """this action replace the selected element with a new element
    """

    # decorations
    # .. name of action factory method
    factory_method = 'replaceBy'

    # attributes
    newelement = descriptors.object()

    def identify(self, inspector):
        return inspector.onReplaceElement(self)
    


class ElementSetAttribute(base):

    """this action set attribute of the selected element to a new value
    """

    # decorations
    # .. name of action factory method
    factory_method = 'setAttr'

    # attributes
    attrs = descriptors.dict()

    def identify(self, inspector):
        return inspector.onElementSetAttribute(self)

# need a special factory method to simplify the syntax
def setAttr(self, **kwds):
    return ElementSetAttribute(element=self, attrs = kwds)
from luban.ui.actions.ElementActionFactory import ElementActionFactory
ElementActionFactory.setAttr = setAttr


# End of file 
