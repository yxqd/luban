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
class Dict(Type):
    """
    The Dict type declarator
    Dict: a dictionary
    """

    # interface
    @classmethod
    def __cast__(cls, value, **kwds):
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
