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


from luban.content._accountant import getElementClasses


def filterElementTypes(filter_function, getTypes=getElementClasses):
    types = getTypes()
    return filter(filter_function, types)


def getTeleContainerTypes():
    from luban.content.TeleContainer import TeleContainer
    f = lambda klass: issubclass(klass, TeleContainer)
    return filterElementTypes(f)


def getElementtypes_Noroot():
    from luban.content.ElementNotRoot import ElementNotRoot
    f = lambda klass: issubclass(klass, ElementNotRoot)
    return filterElementTypes(f)
    

# version
__id__ = "$Id$"

# End of file 
