.. _form-tutorial:

Forms
-----

Create a luban project::

 $ cd /somewhere
 $ luban create formdemo


.. note::
   Before starting this new project, make sure you have already shut down other
   projects that might be using the same port; otherwise you will get
   an error message suggesting you use a different port.

Then start this new project::

 $ luban start formdemo


Add a form
==========
Let us now make some modifications to the interface.

Use your favorite editor to edit formdemo/python/formdemo/actors/start.py
and change it into::

 import luban
 from luban.controller.Actor import Actor as base
 
 class Actor(base):
 
     expose = 1
 
     def default(self):
         frame = luban.e.frame(title="luban form test")
         doc = frame.document(title="form")
 
         # form
         form = doc.form(title='test form')

         # fields
         # .. check boxes
         checkbox1 = form.checkbox(
             name='boolvar1', label='check box 1', checked=False)

         checkbox2 = form.checkbox(
             name='boolvar2', label='check box 2', checked=True)

         # .. text field
         textfield = form.text(label='textfield', name='textvar')
        
         # submit button
         submit = form.submitbutton(label='submit')

         # action when form is submitted
	 form.onsubmit = luban.a.alert('submitted')
	 	 
         return luban.a.establishInterface(frame)

Refresh your browser and it should bring you to something similar to this:

.. figure:: images/form.png
   :scale: 70%

   Figure 1. A form


If you click the submit button, an alert box will pop up with the message
"submitted".

However, this does not really send any form data to the "server side".
We need to modify the "onsubmit" event handler a bit to make that happen.
Change::
 
	 form.onsubmit = luban.a.alert('submitted')

to ::
 
         form.onsubmit = luban.a.load(
             actor = self.name,
             routine = 'process',
             kwds = luban.event.data,
             )

and add the following method to the start actor::
 
     def process(self, **kwds):
         msg = "submitted: %s" % (kwds,)
         return luban.a.alert(msg)

The start.py will look like::

 import luban
 from luban.controller.Actor import Actor as base
 
 class Actor(base):
 
     expose = 1
 
     def default(self):
         frame = luban.e.frame(title="luban form test")
         doc = frame.document(title="form")
 
         # form
         form = doc.form(title='test form')

         # fields
         # .. check boxes
         checkbox1 = form.checkbox(
             name='boolvar1', label='check box 1', checked=False)

         checkbox2 = form.checkbox(
             name='boolvar2', label='check box 2', checked=True)

         # .. text field
         textfield = form.text(label='textfield', name='textvar')
        
         # submit button
         submit = form.submitbutton(label='submit')

         # action when form is submitted
         form.onsubmit = luban.a.load(
             actor = self.name,
             routine = 'process',
             kwds = luban.event.data,
             )
	 	 
         return luban.a.establishInterface(frame)
	 
	 
     def process(self, **kwds):
         msg = "submitted: %s" % (kwds,)
         return luban.a.alert(msg)

After you refresh your browser, you can try to change the values of the form controls 
and then submit the form. 
You will be prompted with an alert message box like this:

.. figure:: images/form-data-submit-alert.png
   :scale: 100%

   Figure 2. form data is submitted to the "server side", and then an action
   is returned from the handling routine that asks to show an
   alert message box with the submitted data.

For in-depth discussion about using forms, 
please go to :ref:`Working with form <user-guide-working-with-form>`.

More
====
Continue to :ref:`next tutorial "Make your web application dynamic" <dynamic-ui-tutorial>`

or back to 
:ref:`"Tutorials" <user-tutorials>`

or back to
:ref:`"User Guide" <user-guide>`
