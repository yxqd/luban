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


# base class
from pyre.schema.Type import Type


class List(Type):
    """
    The List type declarator
    List: a list of strings
    """

    # interface
    @classmethod
    def pyre_cast(cls, value, **kwds):
        """
        Convert {value} into a list of strings
        """
        import collections

        # split the string
        if isinstance(value, str):
            value = list(value.split())
        # if {value} is an iterable, convert it to a list and return it
        if  isinstance(value, collections.Iterable):
            return list(str(v) for v in value)
        # otherwise flag it as bad input
        raise cls.CastingError(value=value, description="unknown type: value={!r}".format(value))



class Dict(Type):
    """
    The Dict type declarator
    Dict: a dictionary
    """

    # interface
    @classmethod
    def pyre_cast(cls, value, **kwds):
        """
        Convert {value} into a list of strings
        """
        # split the string
        if isinstance(value, str):
            value = eval(value)
        # if {value} is an dict, good
        if  isinstance(value, dict):
            return value
        # otherwise flag it as bad input
        raise cls.CastingError(value=value, description="unknown type: value={!r}".format(value))


# version
__id__ = "$Id$"

# End of file 
