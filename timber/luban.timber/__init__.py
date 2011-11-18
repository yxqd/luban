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
from . import luban_ext
from . import controller # replace the core controllers with timber controllers. see eg .controllers.CherrypyController


from .controller import setUploadPath


# End of file 
