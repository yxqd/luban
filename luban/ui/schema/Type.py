# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


class Type:
    """
    The base class for type declarators
    """


    # interface
    @classmethod
    def __cast__(cls, *args, **kwds):
        """
        Convert the given value into the native type i represent
        """
        raise NotImplementedError(
            "class {.__name__!r} must implement '__cast__'".format(cls))
    

    # exception
    from .exceptions import CastingError


# end of file 
