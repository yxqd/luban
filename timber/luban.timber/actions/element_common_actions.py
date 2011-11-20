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



class HideElement(base):

    """this action hide an element
    """

    # decorations
    # .. name of action factory method
    factory_method = 'hide'

    # attributes

    def identify(self, inspector):
        return inspector.onHideElement(self)



class ShowElement(base):

    """this action show an element
    """

    # decorations
    # .. name of action factory method
    factory_method = 'show'

    # attributes

    def identify(self, inspector):
        return inspector.onShowElement(self)



class AppendElement(base):
    
    # decorations
    # .. name of action factory method
    factory_method = 'append'

    # attributes
    newelement = descriptors.element() 

    def identify(self, inspector):
        return inspector.onAppendElement(self)
    
    

class InsertAfterElement(base):
    
    # decorations
    # .. name of action factory method
    factory_method = 'after'

    # attributes
    newelement = descriptors.element()

    def identify(self, inspector):
        return inspector.onInsertAfterElement(self)
    
    

# End of file 
