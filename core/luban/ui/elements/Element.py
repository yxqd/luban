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


from luban import journal
debug = journal.debug('luban.ui.elements.Element')


from .ElementBase import ElementBase, Meta as MetaBase
class Meta(MetaBase):

    def __new__(cls, name, bases, attributes, **kwds):
        # collect event types and add event handlers
        from ..Event import Event
        from ..descriptors import eventhandler
        for k, v in attributes.items():
            try: 
                isevent = issubclass(v, Event)
            except TypeError:
                continue
            if not isevent:
                continue
            key = 'on' + k
            descriptor = eventhandler(eventtype=v)
            # don't override
            if key not in attributes:
                attributes[key] = descriptor
            continue

        # the created class
        created = super().__new__(cls, name, bases, attributes, **kwds)

        # doc for constructor
        created.__init__.__doc__ = created.getCtorDocStr()

        return created


class Element(ElementBase, metaclass=Meta):

    """base class of all element types except null element
    """
    
    # indicate this is abstract and cannot be instantiated
    abstract = True

    # what are the possible parent element types?
    # this is usually any element container types, but
    # special cases exist. see, for example, Frame and Tabs.Tab
    parent_types = 'any' 

    # what are the possible child element types?
    child_types = 'any'
    
    # common ui element properties
    id = descriptors.id()
    id.tip = 'Identifier of this element. need to be unique among all elements'
    
    name = descriptors.str()
    name.tip = 'Name of this element. must be unique among siblings'

    # XXX: class is reserved. what would be a better name?
    Class = descriptors.list()
    Class.tip = 'Class of this element. Useful for styling the element'

    # events -- must have one-one correspondence with event handler
    from ..Event import Event
    class click(Event):
        # decorations
        simple_description = "event happens when a ui element is clicked"
        __unique_type_name__ = 'click'
        # no attributes
    del Event
    
    # ************************************************************
    # event handlers
    # event handlers will be automatically defined using event types
    # defined here (like "click" event above will cause a "onclick"
    # event handler automatically)
    # here is just an example in case one has to define a custom 
    # event handler descriptor
    # onclick = descriptors.eventhandler()
    # onclick.tip = 'action when a mouse click happens on this element'
    # ************************************************************    
    
    def addClass(self, kls):
        "add a classifier for this element"
        classes = self.Class
        if kls not in classes: 
            classes.append(kls)
        return self
    
    
# version
__id__ = "$Id$"

# End of file 
