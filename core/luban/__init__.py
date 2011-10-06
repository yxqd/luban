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


__doc__ = """
luban: generic user interface specification

packages:

* ui: type system; element and action representations
* weaver: convert luban ui representation to implementations such as javascript
* utils: miscellaneous tools

"""

# settings
import os
# .. whether pyre is available
has_pyre = os.environ.get('LUBAN_HAS_PYRE') or os.environ.get('HAS_PYRE')
# .. allow extension to override element/action definitions without
# .. throwing exceptions
extension_allow_override = False
# .. use default extension "timber"
use_timber_extension = os.environ.get('LUBAN_USE_TIMBER')
use_timber_extension = eval(use_timber_extension) \
    if use_timber_extension is not None \
    else True
# .. debug on/off
debug = True


#
from .ui import e, a, event

#
from . import decorators

#
if use_timber_extension:
    import luban.timber

# End of file 

