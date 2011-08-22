# -*- coding: utf-8 -*-
#
# Jiao Lin
# california institute of technology
# (c) 2006-2011 all rights reserved
#


from .Type import Type


class Action(Type):
    """ui action type
    """
    
    
    # interface
    @classmethod
    def __cast__(cls, value, **kwds):
        from ..actions.ActionBase import ActionBase
        if not isinstance(value, ActionBase):
            msg = "{!r}".format(value)
            raise ValueError(msg)
        return value


# end of file 
