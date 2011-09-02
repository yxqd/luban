# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


jui_root = 'jquery/jquery-ui-1.8.16'
jui_dev = '%s/development-bundle' % jui_root
jui_external = '%s/external' % jui_dev
jui_deps = [ 
    '%s/%s' % (jui_external, dep) 
    for dep in ['qunit.js',
                'jquery.metadata.js',
                'jquery.cookie.js',
                'jquery.bgiframe-2.1.2.js',
                ]
    ]
jui_core = [
    '%s/ui/%s' % (jui_dev, f)
    for f in ['jquery.ui.core.js',
              'jquery.ui.widget.js',
              'jquery.ui.mouse.js',
              'jquery.ui.position.js',
              'jquery.ui.draggable.js',
              'jquery.ui.resizable.js',
              ]
    ]

luban_core = [
    'luban/luban-core.js',
    'luban/luban-controller.js',
    'luban/luban-credential.js',
    'luban/luban-compiler-preloader.js',
    'luban/luban-actioncompiler.js',
    'luban/luban-documentmill.js',
    'luban/luban-widget-core.js',
    ]

base = {
    'stylesheets': 
    (
    'jquery-ui-1.8.16/ui-lightness/jquery-ui-1.8.16.custom.css',
    'luban.css',
    ),
    
    'javascripts':
        ['jquery/jquery-1.6.2.min.js',] \
        + jui_deps \
        + jui_core \
        + luban_core
    }

application = {
    }

tabs = {
    'javascripts':
    (
    '%s/ui/%s' % (jui_dev, 'jquery.ui.tabs.js'),
    ),
    }


__all__ = ['base', 'application', 'tabs']


# version
__id__ = "$Id$"

# End of file 
