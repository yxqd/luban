.. _helloworld:

Hello world!
------------

Install::

 $ easy_install luban


Create a luban project::

 $ cd /somewhere
 $ luban create helloworld


Start this new project::

 $ luban start helloworld

A server will be running to serve your web application,
and a browser will be started to show the webpage.


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
Now you can refresh the browser that was opend automatically earlier
and see the changes.


A few concepts
==============



