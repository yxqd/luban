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
#
# To add an element
# 1. add this name of the elemen to the list "elements"
# 2. add a new dictionary for this element:
#    <element_name> = {"javascripts": ..., "stylesheets": ...}
#
# For riveted elements, make sure to do the same for both
# the container element and the sub element.
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
    'slides', 'slide',
    ]
            
for element in elements:
    d = {'javascripts': ('luban.timber/widgets/%s.js' % element,)}
    exec ("%s=d" % element)
    continue

# del d, element, elements


accordion = {
    'javascripts':
        (
        '%s/ui/%s' % (jui_dev, 'jquery.ui.accordion.js'),
        
        'luban.timber/widgets/accordion.js',
        ),
    }


from .. import jsdb
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
    
    'dep': jsdb.prettify,
    }


uploader = {
    'javascripts':
        (
        'jquery.ext/jquery.iframe-transport.js',
        'jquery.ext/blueimp-file-upload/jquery.fileupload.js',
        '%s/ui/%s' % (jui_dev, 'jquery.ui.progressbar.js'),
        
        'luban.timber/widgets/uploader.js',
        ),
    'stylesheets':
        (
        'jquery.ext/blueimp-file-upload/jquery.fileupload-ui.css',
        ),
    'dep': jsdb.blueimp_fileupload,
    }


slides = {
    'javascripts':
        (
        'jquery.ext/jquery.cycle.all.js',

        'luban.timber/widgets/slides.js',
        ),
    'stylesheets':
        (
        ),
    'dep': jsdb.jquery_cycle,
    }


__all__ = core + elements


# version
__id__ = "$Id$"

# End of file 
