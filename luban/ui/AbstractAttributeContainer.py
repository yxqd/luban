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

    """This defines the interface of the attribute containers
    that are used to store specifications of ui elements and
    ui actions.

    The implementation makes heavy use of descriptors so that
    it is easy to introspect the elements/actions to do different
    things.
    """

    # interface to descriptors are the important for inspectors
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

    
    # double dispatching for inspector
    def identify(self, inspector):
        e = "class %r should implement 'identify'" % self.__class__.__name__
        raise NotImplementedError(e)
    

    def __init__(self, name=None):
        self.name = name
        return

    pass


# version
__id__ = "$Id$"

# End of file 
