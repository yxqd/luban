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
luban ui elements

TODO:

* fix registerElementProvider
"""


def registerElementProvider(provider):
    from ._registry import element_providers as providers
    providers.append(provider)
    return providers


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


# create element factory methods
from ._registry import fundamental_elements
for name in fundamental_elements:
    klass = fundamental_elements.getElementClass(name)
    # make a lower case alias 
    code = '%s = klass' % name.lower()
    exec(code)
    continue


__all__ = [
    'registerElementProvider',
    ] \
    + [e.lower() for e in elementtypes]
# + elementtypes \


# End of file 
