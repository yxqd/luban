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


from luban import journal
debug = journal.debug('luban.ui.elements.ElementBase')


from .AttributeContainer import AttributeContainer, Meta


class ElementBase(AttributeContainer, metaclass=Meta):

    """base class for all ui element types"""
    
    # indicate this is abstract and cannot be instantiated
    abstract = True

    # don't override this
    lubanelement = descriptors.bool(default=True)
    

# End of file 
