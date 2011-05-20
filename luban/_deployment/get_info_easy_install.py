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


from Info import Info
info = Info()


import os

from pkg_resources import resource_filename

# this assumes that etc is actually installed as a data directory of package "luban"
# see luban releaser for details
info.pyre_etc = resource_filename('luban', 'etc')


# this assumes that all luban applications, examples, and test applications
# are installed into the "share" subdir of package "luban"
info.common_html_base = resource_filename('luban.weaver.web', '')


# version
__id__ = "$Id$"

# End of file 

