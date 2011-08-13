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


from luban import _journal as journal
debug = journal.debug('luban.ui.elements.ElementBase')


from .AttributeContainer import AttributeContainer, Meta as _metabase


# meta class
class Meta(_metabase):

    
    def __new__(cls, name, *args, **kwds):
        # call super class to construct the class
        target = super().__new__(cls, name, *args, **kwds)
        
        #
        from ._registry import register
        register(target)
        
        return target
        

class ElementBase(AttributeContainer, metaclass=Meta):

    """base class for all ui element types"""
    
    # indicate this is abstract and cannot be instantiated
    abstract = True
    
    
# version
__id__ = "$Id$"

# End of file 
