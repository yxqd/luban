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


from .luban_js_core import modules as js_modules

css = 'luban.css'

from ..Library import Library
Library(
    'luban.core',
    css = [css],
    javascripts = [ 'luban/%s' % m for m in js_modules ],
    dependencies = ['jqueryui.core'],
    )


# End of file 
