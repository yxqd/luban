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


"""
to developers:
 any public attribute of this module must be a dictionary like this:

 base = {
    'stylesheets': [...],
    'javascripts': [...],
    }

 You could import them from other modules. but please maks sure
 EVERY attribute is a dictionary.
"""


from ..Bundle import Bundle

import luban
if luban.debug:
    from . import jquery1_6_2_debug, jqueryui_1_8_16_debug
    from . import jquery_ext
    from . import luban_core_debug, luban_widgets
    bundle = Bundle(
        base = ['luban.core'],
        tabs = ['luban.widgets.tabs'],
        )
    
else:
    from .jquery1_6_2 import *


# End of file 
