.. _widgets-tutorial:

Adding Widgets to Your Interface
--------------------------------

Create a luban project::

 $ cd /somewhere
 $ luban create widgetsdemo


.. note::
   Before starting this new project, make sure you have already shut down other
   projects that might be using the same port; otherwise you will get
   an error message suggesting you use a different port.

Then start this new project::

 $ luban start widgetsdemo


Adding an Accordion
===================
Now let's make some modifications to the interface.

Use your favorite editor to edit widgetsdemo/python/widgetsdemo/actors/start.py
and change it to::

 import luban
 from luban.controller.Actor import Actor as base
 
 class Actor(base):
 
     expose = 1
 
     def default(self):
         frame = luban.e.frame(title="luban widgets test")
         doc = frame.document(title="accordion")
	 acc = doc.accordion()

         sec1 = acc.section(label='section1')
         sec1.paragraph(text='paragraph in section1')
         
         sec2 = acc.section(label='section2', selected=1)
         doc2 = sec2.document(title='doc in section2')
         doc2.paragraph(text='section 2 text')
    
         sec3 = acc.section(label='section3')
         sec3.paragraph(text='text text text')
    
         return luban.a.establishInterface(frame)

Refresh your browser and it should bring you to something like this:

.. figure:: images/accordion.png
   :scale: 70%

   Figure 1. Accordion widget

You can click on the accordion to see its behavior.


"tabs"
======
Now let us try the widget "tabs". Replace start.py with the following content::

 import luban
 from luban.controller.Actor import Actor as base
 
 class Actor(base):
 
     expose = 1
 
     def default(self):
         frame = luban.e.frame(title="luban widgets test")
         doc = frame.document(title="tabs")

         tabs = doc.tabs()
         tabs.tab('tab1').paragraph(text='tab1 texts')
         tabs.tab('tab2', selected=1).paragraph(text='tab2 texts')
         tabs.tab('tab3').paragraph(text='tab3 texts')
	 
         return luban.a.establishInterface(frame)

Refresh your browser and it should bring you to something like this:

.. figure:: images/tabs.png
   :scale: 70%

   Figure 2. Tabs widget


More Widgets
============

To see more widgets, go to http://lubanui.org/aokuang


More
====
Continue to the :ref:`next tutorial "Forms" <form-tutorial>`

or back to 
:ref:`"Tutorials" <user-tutorials>`

or back to
:ref:`"User Guide" <user-guide>`
