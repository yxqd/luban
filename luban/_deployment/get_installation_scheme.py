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


# if both PYRE_DIR is not defined, suppose luban is installed
# by easy_install
from pyre_getexportroot import pyre_root
if pyre_root:
    scheme = 'mm'
else:
    scheme = 'easy_install'


# version
__id__ = "$Id$"

# End of file 

