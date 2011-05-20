#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin     
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import journal
debug = journal.debug('luban.content.Element')


from AttributeContainer import AttributeContainer



class Element(AttributeContainer):

    abstract = True

    id = AttributeContainer.descriptors.str(name='id')
    id.tip = 'Identifier of this element. If left blank, a unique one will be generated automatically'
    
    Class = AttributeContainer.descriptors.str(name='Class')
    Class.tip = 'Class of this element. Useful for styling the element'
    
    onclick = AttributeContainer.descriptors.eventHandler(name='onclick')
    onclick.tip = 'event handler that triggers when a mouse click happens on this element'
    
    oncreate = AttributeContainer.descriptors.eventHandler(name='oncreate')
    oncreate.tip = 'event handler that triggers when the widget is created on the interface'
    oncreate.experimental = True
    
    onkeypress = AttributeContainer.descriptors.eventHandler(name='onkeypress')
    onkeypress.tip = 'event handler that triggers when user stroke a key and this element is on focus'
    onkeypress.experimental = True
    
    hidden = AttributeContainer.descriptors.bool(name='hidden', default=False)
    hidden.tip = 'If true, this element is hidden'
    
    name = AttributeContainer.descriptors.str(name='name')
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

        for k, v in kwds.iteritems():
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
            raise RuntimeError, "id cannot contain '.': %s" % id

        attributes['id'] = id
        return

    __metaclass__ = AttributeContainer.__metaclass__
    

import GUID

# version
__id__ = "$Id$"

# End of file 
