.. _language-core:

Luban User Interface Language Core
==================================


Assumptions
-----------

A user interface consists of a bunch of separable parts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

The interactions among constituents of a UI may be
extremely complex, but we assume that it is possible
to separate a UI into non-entangled parts where each
part has a clean API.

*Will demonstrate that sophisticated and dynamic UIs
can still be separable.*

Note: to those who have studied quantum field theory, 
this is like renormalization. One can always find the
right way to renormalize a part of the field to make it
not divergent (to encapsulate the possibly divergent
interactions inside one entity).



Principles
----------

Minimalist approach
"""""""""""""""""""
Try to find the most compact conceptual structure
sufficient to describe a sophisticated, dynamic, and mordern
user interface.

As we can see this is the main difference between luban
and other generic UI specification such as UIML.


Implementation agnostic
"""""""""""""""""""""""
The "language" has to be independent of technologies 
for building user interface.


We are only concern with the most essential aspects of user interface
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Visual appeals (eye candys) are not the essential part of UI.



Type system
-----------
Luban has a very limited type system. 
Since it deals only with user interface, it is easy to understand that
many complex types are unecessary.

* primitive types: bool, str, int, float
* list: a list of instances of luban types
* dictionary: key value pairs. key: str type. value: instance of any luban type
* object: generic luban object that defines attributes (name: str, value: instance of any luban type)
 * element (specialized luban object types that describes UI elements)
 * action
 * event


Basic concepts and structure
----------------------------
A user interface is described using a hierarchy structure
consisting of ui elements.

A controller is responsible for constructing and returning
instances of luban types upon request. 

A request is identified by its parameters (e.g. "actor", "routine", ...)

There is no real reason that there could not be more than 1
controller. But here we assume only one controller exists, 
for simplicity of this discussion.

A user interface starts by a request to the UI controller
whose response is a UI element
hierarchy with a root node being of the "Frame" type.
"Frame" is a special UI element type.

User interactions with the UI results in events.

An event will trigger an associated action.

An action could be changing visual representation of
a UI element, or loading some data from the controller
to update a UI element, or loading another action from
controller to execute.


Controller
""""""""""
The controller has access to many actors.
When requested for response, the controller delegates
to one of its actors to perform a routine.
This routine will produce a response depending
on whatever extra parameters given to it.

The response always is an instance of a luban type.


Elements
""""""""
A visual element in the user interface.

A ui element has the following attributes:

* properties
* event handlers
* sub elements (for element container only)

Property
********
Examples of properties:

* paragraph.text: the text string for a paragraph element
* <element>.class: similar to the idea of css class. A class of an element can be used by fine tune the styling.
* document.title: the title of a document element


Event handler
*************
An event handler corresponds to one type of event.
For example, "onclick" event handler will be fired when
an element is clicked.

A event handler has to be assigned a null value (in case of python, None),
or an action.


Sub elements
************

Instances of element container types can have sub elements.
For example, a "Document" instance can have a paragraph
as one of its sub elements.
It can also have another document as a sub element.



Frame
*****

Frame is a special type of UI element.
If a routine returns a frame instance, the client
side of the user interface establish a frame, which
is the root of a user interface hierarchy.

A frame element can only be the root of a UI element hierarchy,
and it cannot be a sub element.


An element hierarchy example
****************************

An example::

 + document(title="main document")
 |-- paragraph(text=['some text'])
 |-+ form(title='my form')
   |-- textfield(label='input1', value='initial value')
   |-- textarea(label='input2', value='initial value')
   |-- submitbutton(label='Submit')



Actions
"""""""
"Action" is a category of luban object types that describe
actions that update the UI, or actions to load something
from the controller (which may in the end update the UI as well).

It is worth to reiterate that the action types in luban
are very limited: it is either directly changing the UI,
or ask the controller for information that will lead to 
actions that change the UI. No way is included in luban
to describe complex logic, for example. This is the main 
difference between luban and UIML. 
It is assumed that any complex behavior is either 
absorbed into the API of the UI elements (widgets), or
is performed by an actor of the controller.

An action is an instance of a luban action type, and
it has properties that defines the behavior of the action.

Following are more details of the types of actions


Simple naive actions
********************

* Alert(message=<text>): show an alert window with the given message


Element selector
****************

* SelectByIDandType(id=<id>, type=<optinal>): select an element by its id, and optionally its type


Element actions
***************
Actions that update a UI element. Examples:

* ReplaceContent(element=<element selector>, newcontent=<luban element hierarchy>): replace the content of the given element with the new content


Action to talk to the controller
********************************

* Load(actor=<actor name>, routine=<routine name>, ..extra parameters..)

This action asks the controller to run the given routine of the
given actor with all the extra parameters, and obtain the returned value.

If the returned value is another action, that action will then be performed.
For example, if the returned value is the action::

 Alert(message="hello")

this action will be performed and an alert window will pop up.
Usually what happen will be that the controller will carry out some
computations and depends on the computation result, return an appropriate
action to perform on the user interface side.

The returned value could be an instance of luban types other than an action.
For example, in pseudo code::

 button.onclick = \
   select(id="help-message-window")\
     .replaceContent(
       load(actor="helper", 
            routine="getMessage", 
            topic="Monte Carlo simulations"
           )
     )

Apparantly the returned value from actor "helper", routine "getMessage"
will be a luban UI element hierarchy.
That UI element hierarchy will replace the original content of the
existing UI element that can be identified by its id "help-message-window".


Events
""""""
"Event" is a category of luban object types that describe
events happen to the user interface.

Event data are captured as properties of an event object.

For example::

 TabSelect(oldtab=<old tab id>, newtab=<new tab id>)

is a type of event happens when a tab is selected.


Summary
-------
Up until now, all discusions don't assume any implementation
of the luban specification "language". 
You can see that the core of luban only consists of
luban types that is enough to describe UI elements, actions,
and events. 

In the next section, we will discuss to how to 
program luban with python. 



next: :ref:`programming-luban-with-python`


