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
from luban.weaver.web.libraries import luban_core

lib = Library.get('luban.core')
lib.css += [
    'luban.timber.css',
    ]
lib.javascripts += [
    'luban.timber/luban.timber-core-mini.js',
    ]
lib.dependencies += [
    # history
    'jquery.history',
    ]


# End of file 
