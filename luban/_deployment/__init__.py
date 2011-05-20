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
This 'private' package deal with the installation of luban.
luban needs some resources to function correctly.
This package try to deal with different kind of installation scheme.
"""

import os

from get_installation_scheme import scheme

module = 'get_info_' + scheme
info = None
code = 'from %s import info' % module
exec code
assert info, "module %r does not define deployment info" % module

# override pyre system etc directory
pyre_etc = info.pyre_etc
from pyre.inventory.odb import prefix
prefix._SYSTEM_ROOT = pyre_etc



# version
__id__ = "$Id$"

# End of file 

