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
    'Accordion',
    'AppMenuBar',
    'CodeEditor',
    'CodeViewer',
    'Credential',
    'Dialog',
    'Dock',
    'Document',
    'Downloader',
    'File', 
    'Form',
    'Frame',
    'Grid',
    'HtmlDocument',
    'Image',
    'Link',
    'NewsTicker',
    'Paragraph',
    'Plot2D',
    'Portlet',
    'ProgressBar',
    'ReStructuredTextDocument',
    'Splitter',
    'Tabs',
    'TreeView',
    'Uploader',
    ]
elementtypes = [
    'Button',
    'Document',
    'Frame',
    'Splitter',
    'Tabs',
    'Toolbar',
    ]
def registerAllElements():
    modules = elementtypes
    for name in modules:
        __import__(name, fromlist=['.'], globals=globals())
        continue
    return
registerAllElements()


# create element factory methods
from ._registry import fundamental_elements
for name in fundamental_elements:
    klass = fundamental_elements.getElementClass(name)
    # make a lower case alias 
    code = '%s = klass' % name.lower()
    exec(code)
    continue


# alias
# rstdoc = restructuredtextdocument


# version
__id__ = "$Id$"

# End of file 
