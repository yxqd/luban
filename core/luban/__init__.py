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
* project: luban project
* utils: miscellaneous tools

"""

# settings
import os
# .. whether pyre is available
has_pyre = os.environ.get('LUBAN_HAS_PYRE') or os.environ.get('HAS_PYRE')
# .. allow extension to override element/action definitions without
# .. throwing exceptions
extension_allow_override = False
# .. debug on/off
debug = True


# shortcuts
from .ui import e, a, event
from . import decorators
from .uuid import uuid


#
def load_extensions(extensions):
    from .weaver.web.libraries.default import base
    for ext in extensions:
        module = '%s.luban_ext' % ext
        module = __import__(module, fromlist = [''])
        
        # 
        if hasattr(module, 'jsfiles_toload_onstart'):
            base['javascripts'] += module.jsfiles_toload_onstart
            pass
        
        continue
    return


# End of file 

