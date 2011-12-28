# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Type import Type


class String(Type):
    """
    A class declarator for strings
    """


    # interface
    @classmethod
    def __cast__(cls, value, **kwds):
        """
        Attempt to convert {value} into a string
        """
        try:
            return str(value)
        except Exception as error:
            raise cls.CastingError(value=value, description=str(error))


# end of file 
