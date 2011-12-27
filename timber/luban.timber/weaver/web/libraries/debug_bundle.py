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


from luban.weaver.web.libraries import jquery1_6_2_debug, jqueryui_1_8_16_debug
from . import jquery_ext
from . import blueimp_fileupload, jquery_cycle, prettify
from . import luban_core_debug, luban_widgets


from luban.weaver.web.libraries.debug_bundle import bundle

from .luban_widgets import elements
kwds = {}
for e in elements:
    setattr(bundle, e, ['luban.widgets.%s' % e])
    continue

# End of file 
