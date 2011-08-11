# -*- python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .Type import Type
class OrderedDict(Type):
    """
    The OrderedDict type declarator
    OrderedDict: a dictionary preserving order
    """

    # interface
    @classmethod
    def __cast__(cls, value, **kwds):
        """
        Convert {value} into an ordered dict
        """
        # split the string
        if isinstance(value, str):
            raise NotImplementedError
        import collections
        # if {value} is a list, assume it can be casted to od
        if isinstance(value, list):
            return collections.OrderedDict(value)
        # if {value} is an ordered dictionary, good
        if  isinstance(value, collections.OrderedDict):
            return value
        # otherwise flag it as bad input
        raise cls.CastingError(value=value, description="unknown type: value={!r}".format(value))


# version
__id__ = "$Id$"

# End of file 
