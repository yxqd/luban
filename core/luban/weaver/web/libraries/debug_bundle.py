# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from ..Bundle import Bundle

from . import jquery1_6_2_debug, jqueryui_1_8_16_debug, jqueryui_widgets
from . import jquery_ext
from . import luban_core_debug, luban_widgets
bundle = Bundle(
    base = ['luban.core'],
    tabs = ['luban.widgets.tabs'],
    )
    
# End of file 
