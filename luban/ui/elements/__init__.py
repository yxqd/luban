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
    from ._accountant import element_providers as providers
    providers.append(provider)
    return providers


# elements
elementtypes = [
    'Accordion',
    'AppMenuBar',
    'Button',
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
    'Toolbar',
    'TreeView',
    'Uploader',
    ]
for name in elementtypes:
    code = '''
def %s(*args, **kwds):
    from .%s import %s
    return %s(*args, **kwds)
''' % (name.lower(), name, name, name)
    try:
        exec(code)
    except:
        raise RuntimeError('faield to execute %s' % code)


# alias
rstdoc = restructuredtextdocument


# version
__id__ = "$Id$"

# End of file 
