#!/usr/bin/env python
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


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from luban import journal
debug = journal.debug('luban.ui.elements.ElementBase')


from .AttributeContainer import AttributeContainer, Meta
# this works for python 2 and 3
ElementBaseBase = Meta('ElementBaseBase', (AttributeContainer,), {'abstract':True})


class ElementBase(ElementBaseBase):

    """base class for all ui element types"""
    
    # indicate this is abstract and cannot be instantiated
    abstract = True

    # don't override this
    lubanelement = descriptors.bool(default=True)
    

# End of file 
