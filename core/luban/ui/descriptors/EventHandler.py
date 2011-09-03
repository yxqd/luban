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


from .Property import Property
class EventHandler(Property):
    """
    special property that handles assignment of event handler
    """

    eventtype = None # 
    
    
    def __set__(self, instance, value):
        # None -> NoAction
        if value is None:
            from ..actions.NoAction import NoAction
            value = NoAction()

        # value has to be an action
        from ..actions.ActionBase import ActionBase
        if not isinstance(value, ActionBase):
            m = "%r is not an action" % value
            raise ValueError(m)

        self._checkEvent(value)
        
        return super().__set__(instance, value)


    def _checkEvent(self, action):
        return EventChecker(self.eventtype).check(action)


from ..InspectorBase import InspectorBase, AttributeContainer
class EventChecker(InspectorBase):

    def __init__(self, eventtype):
        self.eventtype = eventtype
        return
    

    def inspect(self, action):
        try:
            return action.identify(self)
        except AttributeError:
            return self.onAny(action)
    check = inspect

    
    def onGetAttr(self, action):
        entity = action.entity
        from ..Event import Event
        if not isinstance(entity, Event):
            return
        if action.name not in self.eventtype.iterDescriptorNames():
            m = "%r is not an attribute of event type %r" % (
                action.name, self.eventtype.__unique_type_name__)
            raise EventAttributeError(m)


class EventAttributeError(Exception): pass


# End of file 
