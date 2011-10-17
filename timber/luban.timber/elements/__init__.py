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


"""
timber elements.

TODO:
* There are still quite a few elements are not yet ported to 0.4:
  they are commented out in the "elementtypes" list.
"""


def registerElementProvider(provider):
    from ._registry import element_providers as providers
    providers.append(provider)
    return providers


# elements
elementtypes = [
    # necessary for aokuang.timber
    'Accordion',
    'Portlet',
    'CodeViewer',

    #
    # 'AppMenuBar',
    'BulletinBoard',
    # 'CodeEditor',
    # 'Credential',
    # 'Dialog',
    # 'Dock',
    # 'Document',
    # 'Downloader',
    # 'File', 
    'Form',
    'Grid',
    'Image',
    # 'Link',
    # 'NewsTicker',
    'ProgressBar',
    'Slides',
    'Toolbar',
    # 'TreeView',
    'Uploader',
    # 'XYPlot',
    ]
def importAllElements():
    modules = elementtypes
    for name in modules:
        __import__(name, fromlist=['.'], globals=globals())
        continue
    return
importAllElements()
del importAllElements


# alias
from luban.ui import e
e.rstdoc = e.restructuredtextdocument


# version
__id__ = "$Id$"

# End of file 
