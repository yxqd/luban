.. _user-guide:

Luban User Guide
================

Luban strives to provide a simple, natural way of creating 
user interface that can be sophisticated and provide
good user experiences.

Please start by trying out 

* :ref:`Tutorials <user-tutorials>`


Basic user interface construction
---------------------------------

Establish a user interface
""""""""""""""""""""""""""

A special luban action is dedicated to establishing a user interface::

 >>> frame = luban.elements.frame(title="my user interface")
 >>> action = luban.actions.establishInterface(frame)

The first statement creates a frame, which is a UI element.

The second statement creates an action that, when executed,
establish a user interface that has a frame with a title "my user interface".


Actor and url
"""""""""""""
To really have the interface showing up in the browser,
you will need an actor.
A simple actor looks like this::

 import luban
 
 from luban.controller.Actor import Actor as base
 class Actor(base):
 
     expose = 1
 
     def default(self):
         frame = luban.elements.frame(title="my user interface")
         return luban.actions.establishInterface(frame)

Save it as "test.py" under directory "helloworld/python/helloworld/actors"
of the helloworld example you got when you ran the
:ref:`helloworld tutorial <helloworld>`.

Now point your browser to ::

 http://localhost:8080/test

You should see a new browser window showing up with a title "my user interface"
and an empty page.

If you change the url to ::

 http://localhost:8080/test/default

you will see the same page.

Here you can see how the actor name and method name maps into the url::

 http://<site-url>/<actor-name>/<method-name>

The "actor-name" and "method-name" both defaults to "default", if they are not
specified.

If there are additional parameters to a method in the actor, it will be also added
to the url. 

* for non-keyword arguments, the url takes the form of ::

    http://<site-url>/<actor-name>/<method-name>/<arg1>/<arg2>/...

  and they are passed to the method sequentially.
* for keyword arguments, the url takes the form of ::

    http://<site-url>/<actor-name>/<method-name>/?key1=val1&key2=val2&...

* for a mix of non-keyword and keyword arguments,
  non-keyword arguments are in front of keyword arguments in the url ::

    http://<site-url>/<actor-name>/<method-name>/<arg1>/<arg2>/.../?key1=val1&key2=val2&...

Examples:

* http://localhost:8080/test/validate/abc
  calls ::

    actors/test.py:Actor().validate(abc)

* http://localhost:8080/test/validate/?username=abc
  calls ::

    actors/test.py:Actor().validate(username=abc)

* http://localhost:8080/test/validate/registration/?username=abc&email=a@b.com
  calls ::

    actors/test.py:Actor().validate("registration", username="abc", email="a@b.com")


Create a user interface hierarchy
"""""""""""""""""""""""""""""""""

A luban UI is a hierarchy of UI elements. 
To create this hierarchy, usually one can create the root node first,
and then gradually build up the hierarchy.

For example, this code::

 >>> container = luban.elements.document(title="Welcome")
 >>> container.paragraph(text="welcome to user registration")
 >>> form = container.form()
 >>> hint = luban.elements.paragraph(text="Please input your name")
 >>> form.append(hint)
 >>> firstname = form.text(label='First name', name='firstname')
 >>> lastname = form.text(label='Last name', name='lastname')

creates the following hierarchy::

 + document with a title
   - paragraph to welcome
   + form
     - paragraph of hint
     - text field for first name
     - text field for last name

Two things to note:

* any UI element can be created using factory methods in luban.elements.

    >>> luban.elements.document(...)
    >>> luban.elements.paragraph(...)

* to create a sub element in a container, one can either use directly
  the factory method on the container::

    >>> container.paragraph(...)

  or create the sub-element first and then add it into the container

    >>> p = luban.elements.paragraph(...)
    >>> container.append(p)

.. note::
   Example usages and API of luban most ui elements can be found at
   `aokuang <http://lubanui.org/aokuang>`_

.. note::
   One way to find out all element factories::

   >>> import luban
   >>> dir(luban.elements)


.. note::
   One way to find out all sub-element factories for a container element::

   >>> <container>.elementfactories()

   For example::

   >>> import luban
   >>> doc = luban.elements.document()
   >>> doc.elementfactories()


Assign actions to event handlers
""""""""""""""""""""""""""""""""

To give your user interface dynamic behaviors, you need to 
assign event handlers of UI elements to actions.
Here is an example::

 >>> button.onclick = luban.actions.alert("clicked")

which basically says that if the button got clicked,
an alert dialog will show up with the message "clicked".

The general form of this assignment is

 >>> element.on<event> = <action>

Each UI element type has its own set of event types, 
while there are common events for all element types.

For example, "click" is a common event for every element type.
"submit" is a special event for "form" element.

At `aokuang <http://lubanui.org/aokuang>`_, you can
find demo and API of these events.


Actions
"""""""

All actions can be constructed using factory methods
under "luban.actions". For example::

 >>> luban.actions.load(...)
 >>> luban.actions.alert(...)
 >>> luban.actions.select(...)...


Simple actions
~~~~~~~~~~~~~~

* alert(message): shows a dialog with one message



Actions communicating with controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* load(actor, routine, *args, **kwds): load a luban object from the controller


.. note::
   You can find demos and APIs of "alert" action and "load" action 
   at the "actions" section of menus on the left side of
   `aokuang <http://lubanui.org/aokuang>`_

Other non-element-actions
~~~~~~~~~~~~~~~~~~~~~~~~~

* establishInterface(frame): establish a user interface

.. note::
   One way to list all non-element-actions is::
   
   >>> import luban
   >>> dir(luban.actions)


Element-actions: Actions on UI elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To construct an action on a UI element, a general form is::

 >>> <selector>.<action>(...)

* <selector> selects a UI element.
* <action> is a action factory method.

Examples::

 >>> luban.actions.select(element=paragraph).destroy()
 >>> luban.actions.select(id="authentication-form", type="form").submit()


Selector
^^^^^^^^

* select(element=<element>)

If the UI element instance is in the current scope,
we can use the "element" keyword argument. For example::

 >>> hint = luban.elements.paragraph(text="please input your name")
 >>> select_hint = luban.actions.select(element=hint)


* select(id=<id>, type=None)

You need to make sure the UI element has an unique id when constructed.

The "type" argument is optional, if the action to take 
is a generic action that applies to all UI elements.
If the action to be taken is only valid for a specific type of UI element,
you have to specify the type of the element using the "type" keyword
argument. For example::

 >>> luban.actions.select(id="header")
 >>> luban.actions.select(id="authentication-form", type="form")


Action on seletected element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just selecting a UI element won't change the UI.
To apply an action to a UI element, 
first select the element, and then call the action factory
with appropriate arguments. For example::

 >>> luban.actions.select(element=paragraph).destroy()
 >>> luban.actions.select(id="authentication-form", type="form").submit()

You can find demos and APIs of actions for UI element types at 
`aokuang <http://lubanui.org/aokuang>`_. 


Advanced topics
---------------

User interface hierarchy construction
"""""""""""""""""""""""""""""""""""""

Skeleton
~~~~~~~~
You can create a skeleton of user interface, and use it wisely.

For example, the following code creates a skeleton::

 def skeleton():
     frame = luban.elements.frame(title="my interface")
     header = frame.document(id='header'); header.paragraph(text='header')
     body = frame.document(id='body')
     footer = frame.document(id='footer'); footer.paragraph(text='footer')
     return frame

The skeleton consists of a header, a body, and a footer.

Then we can use the skeleton and change the body to sth interesting
when needed::

 def login():
     frame = skeleton()
     body = frame['#body']
     form = body.form(title="login")
     ...
     return frame

.. note::
   You can retrieve a descendent element in the element hierarchy
   by ::

    >>> container['#<id>']  # <id> is the id of the descendent element.

   A less powerful form that can only retrieve direct child element is also provide ::

    >>> container['<name>'] # <name> must be the name of a child element of the container
    
.. note::
   Replace a descendent element or a child element is also possible::
   
    >>> container['#<id>'] = <new-element>
    >>> container['<name>'] = <new-element>

