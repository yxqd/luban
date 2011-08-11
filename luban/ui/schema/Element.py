# -*- coding: utf-8 -*-
#
# Jiao Lin
# california institute of technology
# (c) 2006-2011 all rights reserved
#


from .Type import Type


class Element(Type):
    """ui element type
    """
    
    
    # interface
    @classmethod
    def __cast__(cls, value, **kwds):
        from ..elements.ElementBase import ElementBase
        if not isinstance(value, ElementBase):
            msg = "{!r}".format(value)
            raise ValueError(msg)
        return value


# end of file 
