# -*- python -*-


import luban

# we are going to override the "hide", "show" actions
# it could have been defined in other extensions (for example, luban.timber).
# need this to let luban not to complain
luban.extension_allow_override = True



# define new actions
from luban.ui.actions.ElementActionBase import ElementActionBase as base
class HideElement(base):

    """this action hide an element
    """

    # decorations
    # .. name of action factory method
    factory_method = 'hide'

    # attributes
    speed = descriptors.str()

    def identify(self, inspector):
        return inspector.onHideElement(self)



class ShowElement(base):

    """this action show an element
    """

    # decorations
    # .. name of action factory method
    factory_method = 'show'

    # attributes
    speed = descriptors.str()

    def identify(self, inspector):
        return inspector.onShowElement(self)

