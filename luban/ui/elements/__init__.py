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
"""

example1 = """
from luban.ui import elements as lue
doc = lue.document(title="Hello")
p = doc.paragraph(text="world")
"""

TODO = """
* think about implementing shortcuts to obtain element factories quickly
"""

__doc__ += "Example1:\n" + example1


def registerElementProvider(provider):
    """register a package as luban ui element provider
    provider must be a package or a module which defines method "registerAllElements"
    """
    from ._registry import registerAllElements
    registerAllElements(provider)
    return


# elements
elementtypes = [
    'Document',
    'Frame',
    'Paragraph',
    'Button',
    'Tabs',
    ]
def registerAllElements():
    modules = elementtypes
    for name in modules:
        __import__(name, fromlist=['.'], globals=globals())
        continue
    return
registerAllElements()


__all__ = [
    'registerElementProvider',
    ]


# End of file 
