# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''abstract base class for selector
'''


class Selector(object):

    def __init__(self, id=None, type=None, **kwds):
        self._id = id
        self._type = type
        self.props = kwds
        return


    def __str__(self):
        props = self.props
        propsstr = ['%s=%s' % (k,v) for k,v in props.iteritems()]
        return '%s(id=%s, %s)' % (self._type, self._id, ', '.join(propsstr))


    def click(self):
        'click the selected widget'
        raise NotImplementedError

    
    def type(self, text):
        'type in some text in the selected field'
        raise NotImplementedError


    def select(self, key):
        'for a selector widget, select the option specified by its key'
        raise NotImplementedError


    def getText(self):
        raise NotImplementedError


    def getAttribute(self, name):
        raise NotImplementedError


    def getValue(self):
        raise NotImplementedError


    def expand(self):
        'expand a document. only applicable to documents'
        raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 

