# -*- Python -*-
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


STORE_NAME = "descriptors_store"


import collections


class DescriptorCollector(type):

    @classmethod
    def __prepare__(cls, name, bases, **kwds):
        return collections.OrderedDict()


    def __new__(cls, name, bases, attributes, **kwds):
        d = collections.OrderedDict()
        
        #
        rbases = list(bases)
        rbases.reverse()
        for base in rbases:
            if hasattr(base, STORE_NAME):
                store = getattr(base, STORE_NAME)
                d.update(store)
            continue

        for key, attr in attributes.items():
            if isdescriptor(attr):
                attr.name = key
                d[key] = attr
            continue

        # the created class
        created = super().__new__(cls, name, bases, dict(attributes), **kwds)

        #
        setattr(created, STORE_NAME, d)

        return created



def isdescriptor(candidate):
    from ..descriptors.Descriptor import Descriptor
    return isinstance(candidate, Descriptor)


# End of file 
