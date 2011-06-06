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


class AbstractAttributeContainer(object):

    @classmethod
    def iterDescriptors(cls):
        "iterates over descriptors"
        raise NotImplementedError


    @classmethod
    def getDescriptor(cls, name):
        "get descriptor of given name"
        raise NotImplementedError


    # XXX: should not we just use setattr ?
    def setAttribute(self, name, value):
        "set attribute of given name to the give value"
        raise NotImplementedError


    # XXX: should not we just use getattr ?
    def getAttribute(self, name):
        "get attribute of given name"
        raise NotImplementedError


    def iterAttributes(self):
        """iterates over key,value pairs of all attributes
        """
        raise NotImplementedError
    

    def __init__(self, name=None):
        self.name = name
        return

    pass


# version
__id__ = "$Id$"

# End of file 
