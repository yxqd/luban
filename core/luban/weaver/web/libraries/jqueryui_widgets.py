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


root = 'jquery/jquery-ui-1.8.16'
dev = '%s/development-bundle' % root

from ..Library import Library

widgets = [
    'tabs',
    'accordion',
    'dialog',
    'progressbar',
    ]

for widget in widgets:
    js = '%s/ui/%s' % (dev, 'jquery.ui.%s.js' % widget)
    lib = Library(
        'jqueryui.%s' % widget,
        javascripts = [js],
        dependencies = ['jqueryui.core'],
        website = "http://jqueryui.com/demos/%s" % widget,
        )
    continue


# End of file 
