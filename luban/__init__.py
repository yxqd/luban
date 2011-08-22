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


"""
luban: generic user interface specification

packages:

* ui: luban core. type system. element and action representations
* weaver: convert luban ui representation to implementations such as javascript
* utils: miscellaneous tools
* timber: default extension of luban core

"""

# settings
import os
# whether pyre is available
has_pyre = os.environ.get('LUBAN_HAS_PYRE') or os.environ.get('HAS_PYRE')
# allow extension to override element/action definitions without
# throwing exceptions
extension_allow_override = False


# End of file 

