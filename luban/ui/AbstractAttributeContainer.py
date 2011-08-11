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

    # attribute access
    def setAttribute(self, name, value):
        "set attribute of given name to the give value"
        raise NotImplementedError


    def getAttribute(self, name):
        "get attribute of given name"
        raise NotImplementedError


    def iterAttributes(self):
        """iterates over key,value pairs of all attributes
        """
        raise NotImplementedError

    
    # interface to descriptors are important for inspectors
    @classmethod
    def iterDescriptors(cls):
        "iterates over descriptors"
        raise NotImplementedError


    @classmethod
    def getDescriptor(cls, name):
        "get descriptor of given name"
        raise NotImplementedError


    # double dispatching for inspector
    def identify(self, inspector):
        e = "class {.__name__!r} should implement 'identify'".format(self.__class__)
        raise NotImplementedError(e)
    

    pass


# version
__id__ = "$Id$"

# End of file 
