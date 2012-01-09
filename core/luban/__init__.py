# -*- python -*-
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

version: 1.0dev
documentation: http://lubanui.org

packages:

* ui: type system; element and action representations
* controller: controller of UI
* weaver: convert luban ui representation to implementations such as javascript
* scaffolding: helpers to create luban projects, extensions, etc
* cli: command line interface "luban"
* utils: miscellaneous tools

"""

#
import sys
try:
    py_major_ver = sys.version_info.major
except AttributeError:
    py_major_ver = sys.version_info[0]


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
elements = e
actions = a
from . import decorators
from .uuid import uuid


#
def load_extension(ext):
    """load a luban extension
    
    Be careful with the sequence of loading extensions.
    Extension loaded later coule override the earlier one
    if extension_allow_override is True.
    """
    from .extension import loader
    return loader.load1(ext)


def load_extensions(extensions):
    """load a list of extensions

    Be careful with the sequence of loading extensions.
    Extension loaded later coule override the earlier one
    if extension_allow_override is True.
    """
    from .extension import loader
    return loader.load(extensions)


#
if py_major_ver == 2:
    
    def setup_context(locals):
        from luban.ui import descriptors, validators
        locals['descriptors'] = locals['d'] = descriptors
        locals['validators'] = locals['v'] = validators
        return

else:

    def setup_context(locals): pass


# if in interactive mode, load "timber" by default
if not os.environ.get("LUBAN_WITHOUT_TIMBER"):
    import __main__ as m
    if not hasattr(m, '__file__'):
        try:
            from . import timber
        except ImportError:
            import warnings
            warnings.warn("failed to import luban.timber")


#
from .AppConfig import AppConfig
app_config = AppConfig()
del AppConfig


# End of file 

