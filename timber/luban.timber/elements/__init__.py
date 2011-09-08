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


def registerElementProvider(provider):
    from ._registry import element_providers as providers
    providers.append(provider)
    return providers


# elements
elementtypes = [
    # 'Accordion',
    # 'AppMenuBar',
    # 'CodeEditor',
    # 'CodeViewer',
    # 'Credential',
    # 'Dialog',
    # 'Dock',
    # 'Document',
    # 'Downloader',
    # 'File', 
    # 'Form',
    # 'Frame',
    # 'Grid',
    # 'Image',
    # 'Link',
    # 'NewsTicker',
    # 'Paragraph',
    # 'Plot2D',
    'Portlet',
    # 'ProgressBar',
    'Toolbar',
    # 'TreeView',
    # 'Uploader',
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
