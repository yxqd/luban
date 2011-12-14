How to add a new element type in a luban extension
==================================================

Here we will use the luban.timber extension as an example.


* Define the element type by deriving from an appropriate
  base class. Choose from 

  * luban.ui.elements.SimpleElement.SimpleElement - simple element, not container
  * luban.ui.elements.SimpleContainer.SimpleContainer - simple element container. Most containers should be a subclass of SimpleContainer
  * luban.ui.elements.RivetedContainer - 
  * luban.ui.elements.RivetedSubElement - 

* Make sure that when the luban extension is imported, this new definition is imported.
  See luban.timber/elements/__init__.py for how it is done.

* For each type of media, add support for this new element type.


Web weaver
----------

* Add a javascript module for this new element type, and put it into
  the javascript library for the extension. See, for example, 
  luban.timber/weaver/web/javascripts/luban.timber/widgets/
* For riveted elements, make sure there is one javascript module for the container
  and another for the subelement.
* Make sure this new module and its dependencies are included in the 
  "default web weaver library". See luban.timber.weaver.web.libraries.default
  and make sure the paths specified in the "library" match those
  in the javascript library.



API demo
--------
aokuang is the namespace for the API demo of luban extensions.

The API document will be auto-generated from the element itself, but
you can also create a demo of your new element and it can serve both
as a test case for the element and a demo for your users.

First, add a new subpackage in aokuang.<ext>.actors.
See aokuang.timber.actors.button for an example.

Make sure this new subpackage will be included? or auto-included?
use "category" decoration?

Then in the new subpackage, implement one demo using one module.



JS lib details
--------------


  // actioncompiler handlers
  var lap=luban.actioncompiler.prototype;
  lap.ontabselectaction = function(action) {
    var tab = this.dispatch(action.element);
    tab.select();
  };

