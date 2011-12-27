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

lib = Library.get('luban.core')
lib.css += [
    'luban.timber.css',
    ]
lib.javascripts += [
    'luban.timber/elementactioncompiler.js',
    'luban.timber/widget-base.js',
    'luban.timber/history.js',
    # common utils for form elements
    'luban.timber/widgets/form-element-basic.js',
    ]
lib.dependencies += [
    # history
    'jquery.history',
    ]


# End of file 
