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


from luban.ui.actions.ElementActionBase import ElementActionBase as base, Meta
from luban.ui.actions.ElementActionFactory import ElementActionFactory

# attribute access
# .. setAttr
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
ElementActionFactory.setAttr = setAttr

# .. getAttr
class ElementGetAttribute(base):

    """this action get the value of an attribute of the selected element
    """

    # decorations
    # .. name of action factory method
    factory_method = 'getAttr'

    # attributes
    name = descriptors.str()

    def identify(self, inspector):
        return inspector.onElementGetAttribute(self)

# need a special factory method to simplify the syntax
def getAttr(self, name):
    return ElementGetAttribute(element=self, name=name)
ElementActionFactory.getAttr = getAttr


# effects
# .. hide
class HideElement(base):

    """this action hide an element
    """

    # decorations
    # .. name of action factory method
    factory_method = 'hide'

    # attributes

    def identify(self, inspector):
        return inspector.onHideElement(self)


# .. show
class ShowElement(base):

    """this action show an element
    """

    # decorations
    # .. name of action factory method
    factory_method = 'show'

    # attributes

    def identify(self, inspector):
        return inspector.onShowElement(self)


# manipulations
# .. replaceBy
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
    

# .. append
class AppendElement(base):
    
    # decorations
    # .. name of action factory method
    factory_method = 'append'

    # attributes
    newelement = descriptors.element() 

    def identify(self, inspector):
        return inspector.onAppendElement(self)


# .. destroy
class DestroyElement(base):
    
    # decorations
    # .. name of action factory method
    factory_method = 'destroy'
    
    def identify(self, inspector):
        return inspector.onDestroyElement(self)
    
    
# .. after
class InsertAfterElement(base):
    
    # decorations
    # .. name of action factory method
    factory_method = 'after'

    # attributes
    newelement = descriptors.element()

    def identify(self, inspector):
        return inspector.onInsertAfterElement(self)
    
 
# traversing   
# .. find
#    this action need to have action factories, 
#    so we need ElementActionFactory as a base as well
class FindSubElement(ElementActionFactory, base, metaclass=Meta):
    
    """find a sub element by its name
    """
    
    # decorations
    # .. name of action factory method
    factory_method = 'find'

    # attributes
    name = descriptors.str() 
    name.tip = "name of the sub element. it is assuemd that its name is unique among all descendents."
    
    type = descriptors.str() 
    type.tip = "type of the sub element. this should be given if you need to call a type-specific (not generic) action on this found element."

    def identify(self, inspector):
        return inspector.onFindSubElement(self)
    
    

# End of file 
