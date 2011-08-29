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


    def __getattr__(self, name):
        from .elements._registry import element_types
        e = element_types.getElementClass(name)
        if e is None:
            raise AttributeError(name)
        return e


e = ElementClassProxy()
del ElementClassProxy


# proxy to actions
class ActionClassProxy:

    from .actions import __all__ as static_names 

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


# End of file 
