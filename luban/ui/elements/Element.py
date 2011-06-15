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
class Element(AttributeContainer):
    
    # indicate this is abstract and cannot be instantiated
    abstract = True
    
    
    # standard ui element properties
    id = descriptors.str()
    id.tip = 'Identifier of this element. If left blank, a unique one will be generated automatically'
    
    # XXX: class is reserved. what would be a better name?
    Class = descriptors.list()
    Class.tip = 'Class of this element. Useful for styling the element'
    
    onclick = descriptors.action()
    onclick.tip = 'action when a mouse click happens on this element'
    
    oncreate = descriptors.action()
    oncreate.tip = 'action when the widget is created on the interface'
    oncreate.experimental = True
    
    onkeypress = descriptors.action()
    onkeypress.tip = 'action when user stroke a key and this element is on focus'
    onkeypress.experimental = True
    
    hidden = descriptors.bool(default=False)
    hidden.tip = 'If true, this element is hidden'
    
    name = descriptors.str()
    name.tip = 'Name of this element. must be unique among siblings'

    
    def addClass(self, kls):
        classes = self.Class.split(' ')
        if kls in classes: return
        classes.append(kls)
        self.Class = ' '.join(classes)
        return


    def __init__(self, name=None, attributes=None, **kwds):
        AttributeContainer.__init__(self)
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
