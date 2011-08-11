# -*- coding: utf-8 -*-
#
# Jiao Lin
# california institute of technology
# (c) 2006-2011 all rights reserved
#


from .Type import Type


class Object(Type):
    """
    Object is a generic object in luban's specification language
    Please note, that it is really not a generic python object.
    The luban "object" could be
    
    * instances of simple types such as str, integer, boolean
    * instances of complex types such as list of instances of luban types
    * objects with properties that are instances of luban types
    """
    
    
    # interface
    @classmethod
    def __cast__(cls, value, **kwds):
        return value


# end of file 
