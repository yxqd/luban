# -*- python -*-

static_dir = 'static' # relative path to the directory with all the static web files (js/css/images ...). all files in that directory will be copied into "static" directory of the deployment


# extension of luban weaver web libs
weaver_web_lib_extensions = [
    ('luban.core', {'javascripts': ['lubanext.hideshow.js']})
    ]


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

