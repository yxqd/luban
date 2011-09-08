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


# ************************************************************
# bad bad
import luban
luban.__doc__ += """* timber: default extension of luban core
"""
# ************************************************************


# activate extensions
from . import elements, actions
# .. set default weaver web library
from luban.weaver.web import set_default_library_for_weaver
from .weaver.web.libraries import default
set_default_library_for_weaver(default)
del default, set_default_library_for_weaver


# End of file 
