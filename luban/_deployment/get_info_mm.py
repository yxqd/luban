
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

from pyre_getexportroot import export_root

info.pyre_etc = os.path.join( export_root, 'etc' )

info.common_html_base = os.path.join(export_root, 'gongshuzi', 'html')


# version
__id__ = "$Id$"

# End of file 

