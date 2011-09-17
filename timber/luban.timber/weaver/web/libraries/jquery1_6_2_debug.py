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


from luban.weaver.web.libraries.jquery1_6_2_debug import *
from luban.weaver.web.libraries.jquery1_6_2_debug import jui_dev, __all__ as core

base['javascripts'] += [
    'luban.timber/elementactioncompiler.js',
    'luban.timber/widget-base.js',
    ]


elements = [
    'portlet', 'portletitem',
    'accordion', 'accordionsection',
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

__all__ = core + elements


# version
__id__ = "$Id$"

# End of file 