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


# XXXX
# luban core js lib knows about default position of luban widget js libs
# so "javascripts" is an empty list.
# is this really a good strategy?
# XXXX
from ..Library import Library
Library(
    "luban.widgets.tabs",
    javascripts = [],
    dependencies = ['jqueryui.tabs'],
    )

# End of file 
