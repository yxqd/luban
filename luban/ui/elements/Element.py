#!/usr/bin/env python
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


import journal
debug = journal.debug('luban.content.Element')


from .AttributeContainer import AttributeContainer
class Element(AttributeContainer, metaclass=AttributeContainer.__metaclass__):

    abstract = True

    id = descriptors.str(name='id')
    id.tip = 'Identifier of this element. If left blank, a unique one will be generated automatically'
    
    Class = descriptors.str(name='Class')
    Class.tip = 'Class of this element. Useful for styling the element'
    
    onclick = descriptors.eventHandler(name='onclick')
    onclick.tip = 'event handler that triggers when a mouse click happens on this element'
    
    oncreate = descriptors.eventHandler(name='oncreate')
    oncreate.tip = 'event handler that triggers when the widget is created on the interface'
    oncreate.experimental = True
    
    onkeypress = descriptors.eventHandler(name='onkeypress')
    onkeypress.tip = 'event handler that triggers when user stroke a key and this element is on focus'
    onkeypress.experimental = True
    
    hidden = descriptors.bool(name='hidden', default=False)
    hidden.tip = 'If true, this element is hidden'
    
    name = descriptors.str(name='name')
    name.tip = 'Name of this element. must be unique among siblings'

    
    def identify(self, inspector):
        raise NotImplementedError("class %r should implement 'identify'" % self.__class__.__name__)


    def addClass(self, kls):
        classes = self.Class.split(' ')
        if kls in classes: return
        classes.append(kls)
        self.Class = ' '.join(classes)
        return


    def __init__(self, name=None, attributes=None, **kwds):
        Traceable.__init__(self)

        # name is used by my parent to find me
        name = name or (self.__class__.__name__ + str(id(self)) )

        # this should not be necessary if we are not using pyre Inventory
        # to implement AttributeContainer
        AttributeContainer.__init__(self, name)
        self.name = name

        attributes = attributes or {}
        kwds.update(attributes)

        self._setID(kwds)

        for k, v in kwds.items():
            debug.log('setting attribute %r to %s' % (k,v))
            self.setAttribute(k,v)

        return


    def _setID(self, attributes):
        id = attributes.get('id')

        # no id, generate one
        if not id:
            id = GUID.GUID(self)

        # make sure id is a string
        id = str(id)

        # verify
        if id.find('.') != -1:
            raise RuntimeError("id cannot contain '.': %s" % id)

        attributes['id'] = id
        return


    def getCtorDocStr(cls, descriptors=None):
        if not descriptors:
            descriptors = cls.iterDescriptors()
        l = []
        for descriptor in descriptors:
            name = descriptor.name
            value = descriptor.default
            l.append('%s=%r' % (name, value))
            continue
        return '%s(%s)' % (cls.__name__, ', '.join(l))
    getCtorDocStr = classmethod(getCtorDocStr)
    

from . import GUID

# version
__id__ = "$Id$"

# End of file 
