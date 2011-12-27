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

packages:

* ui: type system; element and action representations
* controller: controller of UI
* weaver: convert luban ui representation to implementations such as javascript
* scaffolding: helpers to create luban projects, extensions, etc
* cli: command line interface "luban"
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
    from .weaver.web.libraries.default import bundle as lib_bundle
    from .weaver.web.Library import Library
    
    module = '%s.luban_ext' % ext
    module = __import__(module, fromlist = [''])
    # 
    if hasattr(module, 'weaver_web_lib_extensions'):
        for name, exts in module.weaver_web_lib_extensions:
            Library.get(name).extends(**exts)
            continue
        pass
    
    # obsolete
    if hasattr(module, "jsfiles_toload_onstart"):
        import warnings
        warnings.warn("jsfiles_toload_onstart is obsolete. use weaver_web_lib_extensions")

    return


def load_extensions(extensions):
    """load a list of extensions

    Be careful with the sequence of loading extensions.
    Extension loaded later coule override the earlier one
    if extension_allow_override is True.
    """
    for ext in extensions:
        load_extension(ext)
        continue
    return


# if in interactive mode, load "timber" by default
if not os.environ.get("LUBAN_WITHOUT_TIMBER"):
    import __main__ as m
    if not hasattr(m, '__file__'):
        try:
            from . import timber
        except ImportError:
            import warnings
            warnings.warn("failed to import luban.timber")
        
        
# End of file 

