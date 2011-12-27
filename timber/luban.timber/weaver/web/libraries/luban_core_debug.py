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


from luban.weaver.web.Library import Library
from luban.weaver.web.libraries import luban_core_debug

from .luban_timber_core_js_modules import modules as js_mods

lib = Library.get('luban.core')
lib.css += [
    'luban.timber.css',
    ]
lib.javascripts += ['luban.timber/%s' % m for m in js_mods]

lib.dependencies += [
    # history
    'jquery.history',
    ]


# End of file 
