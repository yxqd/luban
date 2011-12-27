
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


static_css = "weaver/web/css"
static_javascripts = "weaver/web/javascripts"


# .. set default weaver web library
from luban.weaver.web import set_default_library_bundle_for_weaver
from .weaver.web.libraries import default
set_default_library_bundle_for_weaver(default.bundle)
del default, set_default_library_bundle_for_weaver


# End of file 
