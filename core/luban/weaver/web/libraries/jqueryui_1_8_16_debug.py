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
core = [
    '%s/ui/%s' % (dev, f)
    for f in ['jquery.ui.core.js',
              'jquery.ui.widget.js',
              'jquery.ui.mouse.js',
              'jquery.ui.position.js',
              'jquery.ui.draggable.js',
              'jquery.ui.resizable.js',
              ]
    ]


from ..Library import Library
core = Library(
    'jqueryui.core',
    css = ['jquery-ui-1.8.16/ui-lightness/jquery-ui-1.8.16.custom.css'],
    javascripts = core,
    dependencies = [
    'qunit', 'jquery.metadata', 'jquery.cookie', 'jquery.bgiframe',
    ]
    )


tabs = Library(
    'jqueryui.tabs',
    javascripts = ['%s/ui/%s' % (dev, 'jquery.ui.tabs.js'),],
    dependencies = ['jqueryui.core'],
    )


# End of file 
