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


import os    

# if PYRE_DIR is defined, we are good
export_root = pyre_root = os.environ.get('PYRE_DIR')
if not pyre_root:
    # otherwise, try EXPORT_ROOT
    export_root = os.environ.get('EXPORT_ROOT')
    if export_root:
        pyre_root = export_root


# if both PYRE_DIR and EXPORT_ROOT are not defined, suppose luban is installed
# by easy_install


# version
__id__ = "$Id$"

# End of file 

