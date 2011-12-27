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


import luban
if luban.debug:
    from .debug_bundle import bundle
    
else:
    from .jquery1_6_2 import *


# End of file 
