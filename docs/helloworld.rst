.. _helloworld:

Hello world!
------------

Install luban
=============
luban can be installed by either easy_install (for python3) ::

 $ easy_install luban

or pip (for python3) ::

 $ pip install luban

For more details about installing easy_install/pip, please 
:ref:`click here <installation>`.



Create helloworld
=================

Create a luban project::

 $ cd /somewhere
 $ luban create helloworld


Start this new project::

 $ luban start helloworld

A server will be running to serve your web application,
and a browser will be started to show the webpage:

.. figure:: images/helloworld.png
   :scale: 80%

   Figure 1. Hello world application


Congratulations!!! You have created your first luban user interface!


Modify the interface
====================
Let us now make some minor modifications to the interface.

Use your favorite editor to open helloworld/python/helloworld/actors/default.py.
It reads::
 
 import luban
 from luban.controller.Actor import Actor as base
 
 class Actor(base):
 
     expose = 1
 
     def default(self):
         frame = luban.e.frame(title="hello world")
         frame.document(title="hello world")
         return luban.a.establishInterface(frame)

Let us change it to::

 import luban
 from luban.controller.Actor import Actor as base
 
 class Actor(base):
 
     expose = 1
 
     def default(self):
         frame = luban.e.frame(title="hello world")
         doc = frame.document(title="hello world")
         doc.paragraph(text = "This is my first luban user interface")
         return luban.a.establishInterface(frame)

You will see in the terminal where you start the luban project
the server is reloading to incoporate your changes.
Now you can refresh the browser 
and see the changes.


A few concepts
==============

An actor lives in the "server side" and responds to client requests.

The entry point of a luban application is 
by default the "default" method of the "default" actor.
It should return an "establishInterface" action that establish
the user interface from a "frame" instance.

A user interface is represented by a hierarchical structure of 
UI elements.

The root of this hierarchical structure is a "frame".

To create a frame, use the luban.e.frame factory method::

 >>> frame = luban.e.frame(title="hello world")

.. note::
   luban.e is a proxy to factory methods for creating luban elements.
   while luban.a is a proxy to factory methods for creating luban actions.

Now the interface hierarchy is::

 - frame(title="hello world")

To create sub elements in a frame, call the element factory 
on the frame instance::

 >>> doc = frame.document(title="hello world")

And now the interface hierarchy is::

 + frame(title="hello world")
   - document(title ="hello world")

To create a sub element in the first sub element of the frame,
similarly, you call the element factory on the subelement, "doc"::

 >>> doc.paragraph(text = "This is my first luban user interface")

And now the interface hierarchy is::

 + frame(title="hello world")
   + document(title ="hello world")
     - paragraph(text = "...")


.. note::
   Any element container can create a subelement by calling
   the factory method whose name is the subelement type::

     >>> <container>.<elementtype>

   For example::

     >>> frame.document(...)
     >>> frame.paragraph(...)
     >>> doc.paragraph(...)
     >>> doc.document(...)


Shutting down the server
========================

After finish playing with this "helloworld" example, you could shut
down the server::
 
 $ luban stop /path/to/helloworld

