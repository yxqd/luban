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


__doc__ = \
"""
luban ui elements

Users don't use this package directly, rather they use proxy luban.ui.e:

>>> import luban.ui as lui
>>> document = lui.e.document()

Developers could provide extension of luban elements by subclassing base
classes provided here.

"""

# elements
elementtypes = [
    'Frame',
    'Button',
    'Paragraph',
    'Document',
    'HtmlDocument',
    'ReStructuredTextDocument',
    'Splitter',
    'Tabs',
    ]
def importAllElements():
    modules = elementtypes
    for name in modules:
        __import__(name, fromlist=['.'], globals=globals())
        continue
    return
importAllElements()
del importAllElements


__all__ = []


# End of file 
