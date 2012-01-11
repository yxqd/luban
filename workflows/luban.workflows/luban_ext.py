# to use workflows, we need full feature controller
# overload CherrypyController
from luban.controller import CherrypyController as core_CherrypyController_module
from luban.timber.controller.CherrypyFullController import CherrypyFullController
core_CherrypyController_module.CherrypyController = CherrypyFullController

