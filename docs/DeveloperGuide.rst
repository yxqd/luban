Developer Guide
===============

.. note::
   Misc links:
   
   * buildbot for luban: http://bagua.cacr.caltech.edu:50080


Luban can be extended in several different levels.  


Add a new widget into luban
---------------------------
Supposing the widget is "MyCoolButton", generally you will need to:

#. add a ui element into luban.content python namespace such as luban.content.MyCoolButton.  It should inherit from luban.content.Element at a minimum. 
#. add a handler into luban.weaver.Content2Dict and then add a javascript plugin into luban.weaver.web/javascripts/luban/widgets 
#. add a handler into luban.weaver.wx.Weaver and a plugin into luban.weaver.wx.widgets

Adding a test to aokuang, the test application for luban, would also be useful.  Here are specific details about 

Javascript plugins of luban widgets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Luban widgets rendering are structured as "plugins". They all live under
directory
`luban/weaver/web/javascripts/luban/widgets <http://dev.danse.us/trac/luban/browser/trunk/luban/weaver/web/javascripts/luban/widgets>`_
You can overwrite them to implement your own way of rendering
luban widgets using javascript.

Each widget rendering plugin need to provide the following things:

* luban.documentmill.prototype.on<widgetname>
* luban.elementFactory.<widgetname>



Self check
!!!!!!!!!!
Since all js plugins are loaded dynamically, luban js framework has a mechanism
to check and make sure a js plugin to load correctly. You can provide a method ::

  luban.elementFactory.<widgetname>.selfcheck

in which you can check whether the dependencies of this plugin are loaded.
Take a look at 
`appmenubar plugin <http://dev.danse.us/trac/luban/browser/trunk/luban/weaver/web/javascripts/luban/widgets/appmenubar.js>`_ and look for function::

 widgets.appmenubar.selfcheck
 
Wx plugin
^^^^^^^^^
 

