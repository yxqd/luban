# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

__doc__ = """ luban.ui
"""

example1 = """
import luban.ui as lu

doc = lu.e.document(title="hello", id="mydoc")
doc.onclick = lu.a.select(element=doc).replaceContent(
    newcontent = lu.e.paragraph(text='world'))

"""


TODO = """
* implement the idea of "template". 
  should allow to define "facility" in a subclass of an elementcontainer type,
  and call it a template. those template classes should have 
  a normal "template" attribute that is True.
  instances of a template is a element hierarchy
"""


# proxy to elements
class ElementClassProxy:


    def __dir__(self):
        ret = []

        from .elements._registry import element_types
        for t in element_types.names:
            if t not in ret: ret.append(t)
            continue
        return ret


    def __getattr__(self, name):
        from .elements._registry import element_types
        e = element_types.getElementClass(name)
        if e is None:
            raise AttributeError(name)
        return self.__class__._createElementFactory(name, e)


    @classmethod
    def _createElementFactory(thiscls, name=None, cls=None):
        if not name: name = cls.__unique_type_name__
        def _(*args, **kwds):
            return cls(*args, **kwds)
        _.__doc__ = cls.__doc__ or cls.getCtorDocStr()
        _.__name__ = name
        _.type = cls
        from .elements.decorators import elementfactory
        return elementfactory(_)

    
e = ElementClassProxy()
del ElementClassProxy


# proxy to actions
class ActionClassProxy:

    from .actions import __all__ as static_names

    def __dir__(self):
        ret = []

        for t in self.static_names:
            if t not in ret: ret.append(t)
            continue
        
        from .actions._registry import action_types
        for t in action_types.names:
            if t not in ret: ret.append(t)
            continue
        return ret
    

    def __getattr__(self, name):
        if name in self.static_names:
            from . import actions
            return getattr(actions, name)
        
        from .actions._registry import action_types
        e = action_types.getActionClass(name)
        if e is None:
            raise AttributeError(name)
        return e


a = ActionClassProxy()
del ActionClassProxy


# event (global instance)
from .Event import Event
event = Event()
del Event


# import all element types and action types
from . import elements, actions


__all__ = ['e', 'a', 'event']

# End of file 
