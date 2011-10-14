.. _create-ext-tutorial:

How to create a luban extension
===============================

A luban extension is an extension of luban.
You can create one such extension as a standalone python package,
or just as a part of your python package.
It just needs to have an entry point for luban to understand 
what it provides.

Users can easily put your extension into use, as explained in
the following.

A luban extension provides/overloads one or more new type(s) of 
UI elements/actions/events.
For example, you have a nice jquery widget that you want to share
with other luban users, you can easily wrap your widget using
luban (similar to the idea of wrapping a piece of c++ code with
python-c extension code).


Requirement of a luban extension
--------------------------------
A luban extension is a python package (or subpackage).

It contains 

* python code for defining new or overloaded UI elements, actions, and/or events
* javascript (and possibly css) code for implementing the behavior of the new
  elements, actions, and/or events

Following is a tutorial of creating a luban extension that defines two actions
"hide" and "show" that is slightly different from the default hide/show actions in luban.
After this extension is defined, users of your extension
can do::

  >>> luban.a.select(element=<element>).hide(speed='slow')

while the default version in luban, you can only do

  >>> luban.a.select(element=<element>).hide()

Let us suppose the name of this new luban extension python package is "hideshow".

Create the extension
--------------------
You can create a skeleton::

 $ luban creatext hideshow

This will create a new directory "hideshow". Its hierarchy looks like this::

 + hideshow
   - __init__.py
   - luban_ext.py
   + static
     + javascripts

Here __init__.py is required by python.

The python entry point for luban extension is actually luban_ext.py.
You can add definitions of new luban types there.
(You can also put definitions somewhere else, just be sure to import
those modules in luban_ext.py).

Also this luban_ext.py must define a few variables to let luban know
the details of this extension:

* static_dir: the relative path to the directory with all the static web files (js/css/images). by default, this is set to "static", and there is already a "static" subdirectory in the new extension created by "luban creatext" command
* jsfiles_toload_onstart: a list of javascript files under <static_dir>/javascripts that must be loaded at the start of serving a luban application
  

For this tutorial, we will modify luban_ext.py to look like::

 static_dir = 'static' 

 jsfiles_toload_onstart = [
     'lubanext.hideshow.js',
     ]
 
 
 # define new actions
 from luban.ui.actions.ElementActionBase import ElementActionBase as base
 class HideElement(base):
 
     """this action hide an element
     """
 
     # decorations
     # .. name of action factory method
     factory_method = 'hide'
 
     # attributes
     speed = descriptors.str()
 
     def identify(self, inspector):
         return inspector.onHideElement(self)
 
 
 class ShowElement(base):
 
     """this action show an element
     """
 
     # decorations
     # .. name of action factory method
     factory_method = 'show'
 
     # attributes
     speed = descriptors.str()
 
     def identify(self, inspector):
         return inspector.onShowElement(self)

The code itself is self-explanatory:

* it subclass the ElementActionBase to define two actions
* each action defines a factory method name 
* each action defines an attribute "speed" to indicate the speed of show/hide
* each action defines a method for its inspectors

Now that we have two new actions, we need to implement the javascript
part to make it work in web apps.
Create a new file static/javascripts/lubanext.hideshow.js::

 (function(luban, $) {
 
   // we will need to extend the "actioncompiler" of luban
   // first build an extension object
   var actioncompiler_ext = {
   
     'onhideelement': function(action) {
       // action is the object that contains all specifications of the action

       // ask the action compiler to compile the element selector
       var element = this.dispatch(action.element);
       // get the jquery element
       var jqe = element.jqueryelem; // the jquery element
       // speed
       var speed = action.speed;
       // use jquery to do the work
       jqe.hide(speed);
     }
     
     ,'onshowelement': function(action) {
       // action is the object that contains all specifications of the action

       // ask the action compiler to compile the element selector
       var element = this.dispatch(action.element);
       // get the jquery element
       var jqe = element.jqueryelem; // the jquery element
       // speed
       var speed = action.speed;
       // use jquery to do the work
       jqe.show(speed);
     }
     
   };
   // and merge it into luban actioncompiler
   $.extend(luban.actioncompiler.prototype, actioncompiler_ext);
   
 })(luban, jQuery);

The code is self-explanatory.


Use the extension
-----------------

Create a new luban project or reuse one of your earlier sandbox luban project, 
and do the following:

* make sure the new package you  created, "hideshow", is in python path, so that::

 >>> import hideshow

 works
* edit "conf.py" in the project directory and add 'hideshow'
  into the the "extensions" list
* use the new action in your code.

This example is available for download. Choose from one of the following formats:

* `<tutorials/ext-tutorial-actions.tar.gz>`_
* `<tutorials/ext-tutorial-actions.zip>`_.
