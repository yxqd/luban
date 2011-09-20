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

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# developers please read this:
#
# each dictionary defined here should be in the form of
#   {'javascripts': [js file list],
#    'stylesheets': [css file list],
#   }
#
# base: base of luban web client
# application: application specific
# other dictionaries: each corresponds to one widget
#
# in a "js file list", make sure to order them correctly:
# if b.js depends on a.js, a.js should be in front of b.js
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


from luban.weaver.web.libraries.jquery1_6_2_debug import *
from luban.weaver.web.libraries.jquery1_6_2_debug import jui_dev, __all__ as core

base['javascripts'] += [
    'luban.timber/elementactioncompiler.js',
    'luban.timber/widget-base.js',
    ]
base['stylesheets'] +=  [
    'luban.timber.css',
    ]

elements = [
    #
    'portlet', 'portletitem',
    'accordion', 'accordionsection',
    'codeviewer',
    #
    'toolbar',
    'image',
    'grid', 'gridrow', 'gridcell',
    'uploader',
    ]
            
for element in elements:
    d = {'javascripts': ('luban.timber/widgets/%s.js' % element,)}
    exec ("%s=d" % element)
    continue

# del d, element, elements


accordion = {
    'javascripts':
        (
        'luban.timber/widgets/accordion.js',
        '%s/ui/%s' % (jui_dev, 'jquery.ui.accordion.js'),
        ),
    }


from ..jsdb import prettify
codeviewer = {
    'javascripts':
        (
        'other/prettify/prettify.js',
        'luban.timber/widgets/codeviewer.js',
        ),
    'stylesheets':
        (
        'other/prettify/prettify.css',
        ),
    
    'dep': prettify,
    }


uploader = {
    'javascripts':
        (
        'jquery.ext/jquery.iframe-transport.js',
        'jquery.ext/blueimp-file-upload/jquery.fileupload.js',
        'jquery.ext/blueimp-file-upload/jquery.fileupload-ui.js',
        'luban.timber/widgets/uploader.js',
        ),
    'stylesheets':
        (
        'jquery.ext/blueimp-file-upload/jquery.fileupload-ui.css',
        ),
    }


__all__ = core + elements


# version
__id__ = "$Id$"

# End of file 
