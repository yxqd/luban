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


from luban.weaver.web.libraries.default import *

base['javascripts'] += [
    'luban.timber/elementactioncompiler.js',
    'luban.timber/widget-base.js',
    ]


elements = [
    'toolbar',
    'portlet', 'portletitem',
    'image',
    ]
            
for element in elements:
    d = {'javascripts': ('luban.timber/widgets/%s.js' % element,)}
    exec ("%s=d" % element)
    continue



del d, element, elements


# version
__id__ = "$Id$"

# End of file 
