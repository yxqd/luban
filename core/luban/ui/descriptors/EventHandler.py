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

    eventtype = None # type event this handler is about
    notnull = False # meaning this handler must be assigned to an action
    
    
    def __get__(self, instance, cls):
        v = super().__get__(instance, cls)
        if self.notnull:
            from ..actions.NoAction import NoAction
            if isinstance(v, NoAction):
                msg = "Handler for %r event must be assigned with a valid action" % (
                    self.eventtype)
                raise ValueError(msg)
        return v


    def __set__(self, instance, value):
        if self.notnull and value is None:
            raise ValueError
        
        # None -> NoAction
        if value is None:
            from ..actions.NoAction import NoAction
            value = NoAction()

        # list/tuple
        if isinstance(value, list) or isinstance(value, tuple):
            for item in value:
                self._checkAction(item)
                continue
            return super().__set__(instance, value)

        # value has to be an action
        self._checkAction(value)
        return super().__set__(instance, value)


    def _checkAction(self, action):
        if not isinstance(action, ActionBase):
            m = "%r is not an action" % action
            raise ValueError(m)

        self._checkEvent(action)
        return


    def _checkEvent(self, action):
        return EventChecker(self.eventtype).check(action)


from ..actions.ActionBase import ActionBase



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
