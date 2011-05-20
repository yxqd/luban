.. _gongshuzichapter:

Gongshuzi (experimental)
========================

Gongshuzi is a user interface builder created by using luban.
With Gongshuzi, you can create luban user interface visually,
and it is very easy to run your project as a native
or web application from Gongshuzi.

Here is a `video demo of building "Hello World" <tutorials/video/gongshuzidemo.html>`_.

A demo site (partial functionality of Gongshuzi) is available at `gongshuzi@luban <http://luban.danse.us/cgi-bin/gongshuzi/main.cgi>`_.

To have the full functionality of Gongshuzi, please :ref:`run your own copy of gongshuzi <run-gongshuzi>`.


.. _run-gongshuzi:

Run Gongshuzi
~~~~~~~~~~~~~

Please execute the following commands::

    $ cd <somewhere-in-your-home-directory>
    $ download-luban-project.py gongshuzi
    $ start-luban-project.py gongshuzi



How to Use Gongshuzi
~~~~~~~~~~~~~~~~~~~~

If you have not watched it, here is a video demo of how to use gongshuzi to create and run luban
project:

* `"Hello World" application using Gongshuzi <tutorials/video/gongshuzidemo.html>`_


Entering Gongshuzi, you will see a panel with two tabs, one for selecting one of the
existing projects and another one for creating a new project.

Either selecting an old project or creating a new project will bring 
you into the main interface for gongshuzi, in which you can create and manage
visuals (the visual parts of your interface) and actors (the components
to respond user interactions.


Creating a New Visual
"""""""""""""""""""""

In the menu at the top of the screen, select Visual > New. This creates a new blank visual element that you can add widgets to and displays it on the object tree on the left. 


Adding a Container
""""""""""""""""""

Click on one of the icons in the widget palette, or use the menu at the top of the screen and select from Widgets > Simple Containers. 

You can edit your container's properties, such as its title, by double clicking in the 'Value' column in the object properties table on the right. The Editor will then automatically update to reflect your changes.


Adding a Form Field
"""""""""""""""""""

To add a form field to a container, first click on the container you would like to add it to in either the Editor or the object tree on the left, and the container should become highlighted. Then click on one of the icons under 'Form Fields' in the widget palette, or select from Widgets > Form Fields in the menu at the top of the screen. Again, you can configure your widget using the object properties table on the right.

Note that you can only add widgets to containers, so, for example, you cannot add anything to a form field. You can, however, add a container to a container.
