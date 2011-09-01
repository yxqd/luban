.. _core-implementation-python:

Implementation of luban core in python
======================================

In the previous section :ref:`language-core`, 
we discussed the core concepts of luban "language".
Here we discuss the python implementation of luban core.

Python is a very flexible, efficient language.
Especially suitable for meta-programming.


Python meta class tricks can be used to enforce language rules.

* type check/conversion for attributes
* registration of "types"
* auto-generated factory methods to construct sub elements
* uniform constructor/factory signature
* auto-generated documentation 


Element
-------
All element types are inherited from luban.ui.elements.ElementBase,
which inherites AttributeContainer,
the base class of all luban object types.

Example code to create a simple element type that is not a container::

 from luban.ui.elements.SimpleElement import SimpleElement as base
 
 class Paragraph(base):
 
     # decorations for documentation generation
     simple_description = 'a paragraph of text'
     full_description = ''
     
     # meaning this is a real luban type (not an abstract one)
     # so that the luban type registry will register this type
     abstract = False
     
     # attributes
     # .. properties
     text = descriptors.str()
     text.tip = 'text in the paragraph'
     
     # .. events -- must have one-one correspondence with event handler
     # .. please note that the click event is already defined in the base
     # .. class, we copied the code here just to let you see 
     # .. how an event for an element is defined.
     from luban.ui.Event import Event # event base class
     class click(Event):
         # decorations
         simple_description = "event happens when a ui element is clicked"
         abstract = False 
         __unique_type_name__ = 'click'
         # no attributes
     del Event # no need to keep the event base class in the name space
     # ************************************************************
     # event handlers
     # event handlers will be automatically defined using event types
     # defined here (like "click" event above will cause a "onclick"
     # event handler automatically)
     # here is just an example in case one has to define a custom 
     # event handler descriptor
     # onclick = descriptors.eventhandler()
     # onclick.tip = 'action when a click happens to this element'
     # ************************************************************    
     
     # for inspector
     def identify(self, inspector):
         return inspector.onParagraph(self)

 # this actually should be a common action for all element types
 # here we just use it as an example to show how to create an action
 # type for an element type
 from luban.ui.actions.ElementActionBase import ElementActionBase
 class Destroy(ElementActionBase):
 
     # decorations
     # .. this is a real luban type
     abstract = False
     # .. name of action factory method. so we can do select(element=<element>).destroy()
     factory_method = 'destroy'
 
     # no attributes
 
     # for inspector
     def identify(self, inspector):
         return inspector.onDestroy(self)

There are several decorations of the class that help inspectors
of luban types. 
There are also descriptors of attributes of the "paragraph"
element type.
There is also a method "identify" for customize visitor's handler
on this element.
Please read the inline documents for explanations.

Also note that in the event "click" is defined inside
the Paragraph class 
(actually the event "click" is defined in the Element base class,
and is available for any element types, we just 
copy the code here to show how to define an event type).
This gaurantees that an event handler descriptor will
be automatically defined.

Follow this example, one can easily create his own collection
of ui elements.

Creation of an element container type is the same except that 
the new type needs to inherit from luban.ui.elements.ElementContainer
or one of its subclasses.


Action
------
All action types are inherited from luban.ui.actions.ActionBase,
which inherites AttributeContainer,
the base class of all luban object types.

An example of generic action types is the Loading action::

 from luban.ui.actions.Action import Action as base
 
 class Loading(base):
 
     # decorations
     simple_description = 'load from the UI controller'
     full_description = '...'
     abstract = False
 
     # attributes
     actor = descriptors.str()
     actor.tip = 'The actor that will handle this load action'
     
     routine = descriptors.str()
     routine.tip = 'The routine of the actor that will be called to handle this load action'
 
     params = descriptors.dict()
     params.tip = 'Addtional parameters as a dictionary'
     
     # for inspector
     def identify(self, inspector):
         return inspector.onLoading(self)


All actions types that work on ui elements must inherit 
luban.ui.actions.ElementActionBase.ElementActionBase.
Usually these types should be defined alongside the element type
itself.
See the "Paragraph" example above.


Event
-----

All event types are inherited from luban.ui.Event.Event,
which inherites AttributeContainer,
the base class of all luban object types.

An event class defines properties that carries data of the event.

Example luban.ui.elements.Tabs.Tab.select ::

 class Tab(...):
 
     ...

     from ..Event import Event
     class select(Event):
         # decorations
         simple_description = "event happens when this tab is selected"
         abstract = False
         __unique_type_name__ = 'tabselect'
         # attributes
         oldtab = descriptors.str()
         newtab = descriptors.str()
     del Event

     ...

Please be sure to define events in the element type definition
to trigger meta class machinery to define event handler definition.



Controller
----------
Controller implementation actually depends on the media.

Basically what a controller needs to be able to handle a request
from the user interface client, and ask one of its actors to
perform a routine, and return a response to the client.



More
----

Packages/modules:

* luban.ui.schema: type declarators
* luban.ui.AttributeContainer: base class of all luban object types
 * descriptors define attributes
* luban.ui.elements.ElementBase: base class of all luban element types
 * define event classes to automatically create event handlers
* luban.ui.actions.ActionBase: base class of all action types


Tabs/Tab: RivetedContainer


Event data in actions.
