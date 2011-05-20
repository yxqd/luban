# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban.content.ElementNotRoot import ElementNotRoot


from luban.content._accountant import getElementClasses
Elements = getElementClasses()


from luban.content.Element import Element
#credential is not a real UI element
from luban.content.Credential import Credential

Widgets = filter(lambda k: issubclass(k, Element) and k!=Credential, Elements)

name2type = {}
for w in Widgets: name2type[w.__name__] = w


__all__ = [
    'Element',
    'ElementNotRoot',
    'Elements',
    'Widgets',
    'name2type',
    ]


# version
__id__ = "$Id$"

# End of file 
