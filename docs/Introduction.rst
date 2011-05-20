Introduction
==============

The Luban package provides a generic way of specifying the content (no detailed layout, no styles, no color or sizes etc) of your user interfac (UI) as a hierarchy of UI elements.
The representation is so generic that user interfaces on different "media" (web, native, or ...) can be rendered from this representation using different "weavers". The layout and styles will be specified by style sheets (or similar mechanisms).

The Luban package also provides a generic way to describe "actions", to accompany the UI elements. Those actions are rendered by weavers to codes that can be executed to manipulate the UI elements, or talk to the controller. For web application, the corresponding weaver renders javascripts, while for native applications, the corresponding weaver runs normal python code.

In essence, Luban provides an abstraction layer for user interface building,
so that developers of user interfaces can leverage luban's rendering engines 
(which are extendable) to create sophisticated user interfaces using simple
luban API [#lubanAPIisgeneric]_.

Luban is NOT yet another python-based web framework like
`django <http://www.djangoproject.com/>`_ or
`pylons <http://pylonshq.com/>`_.
Luban UI developers don't have to write any html code or javascript code, and also don't need to write codes that mix html with python using some templating syntax. 
All developers need to write about UI is simple python.
For example, 
`this python module <http://dev.danse.us/trac/luban/browser/trunk/examples/jazzclub/content/components/visuals/base/login.odb>`_
creates a login form.

To create user interfaces, luban UI developers need to focus on the following:

* what are the UI elements (widgets) in the interface and their properties, and
* what are the actions to be taken when a user interaction happens;

they do not need to think about how this interface should be implemented in native environment or web application environment. Luban takes care of those things.

If you want to start trying it right away, please first :ref:`install it <Installation>`, and then 
following :ref:`Tutorials <Tutorials>`.

To understand more about the philosophy in luban, please read
:ref:`concepts in luban <philosophy>`.

To see what luban can do, please go to :ref:`Demos <demos>`.

A full list of widgets, event handlers, and actions can be found
in :ref:`API documentation <API>`.


.. rubric: Footnotes

.. [#lubanAPIisgeneric] At this moment, luban UIs are constructed using luban's python API. But the API is designed generic enough so that it should be easy to support creating luban UIs using structured documents such as xml in the future.
