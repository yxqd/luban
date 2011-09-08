How to add a new element type in a luban extension
==================================================

* define the element type by deriving from an appropriate
  base class. choose from 

  * luban.ui.elements.SimpleElement.SimpleElement - simple element, not container
  * luban.ui.elements.SimpleContainer.SimpleContainer - simple element container. most container should be a subclass of SimpleContainer
  * luban.ui.elements.RivetedContainer - 
  * luban.ui.elements.RivetedSubElement - 

* make sure when the luban extension is imported, this new definition is imported
  see luban.timber/elements/__init__.py how it is done

* for each type of media, add support for this new element type

Web weaver
----------

* add a javascript module for this new element type, and put it into
  the javascript library for the extension. see, for example, 
  luban.timber/weaver/web/javascripts/luban.timber/widgets/
* make sure this new module and its dependencies are included in the 
  "default web weaver library". see luban.timber.weaver.web.libraries.default
  and make sure the paths specified in the "library" matches those
  in javascript library.



API demo
--------
aokuang is the namespace for API demo of luban extensions.

The API document will be auto-generated from the element itself, but
you can create a demo of your new element and it can serve both
as a test case for the element and a demo for your users.

First add a new subpackage in aokuang.<ext>.actors.
See aokuang.timber.actors.button for an example.

Make sure this new subpackage will be included? or auto-included?
use "category" decoration?

Then in the new subpackage, implement one demo using one module.
