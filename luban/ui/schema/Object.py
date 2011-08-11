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
        if not isobject(value):
            msg = "{!r}".format(value)
            raise ValueError(msg)
        
        return value


elemental_types = str, int, bool


def iselemental(candidate):
    #
    for et in elemental_types:
        if isinstance(value, et):
            return True
        continue
    return False


def isattributecontainer(candidate):
    from ..AttributeContainer import AttributeContainer
    return isinstance(candidate, AttributeContainer)


def isobject(candidate):
    if iselemental(candidate):
        return True
    
    #
    if isinstance(candidate, list):
        for e in candidate:
            if not isobject(e): return False
            continue
        return True

    import collections
    if isinstance(candidate, dict) or isinstance(candidate, collections.OrderedDict):
        for k,v in candidate.items():
            if not iselemental(k): return False
            if not isobject(v): return False
            continue
        return True

    return isattributecontainer(candidate)

# end of file 
