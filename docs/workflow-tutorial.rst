.. _workflow-tutorial:

Adding a workflow to Your Interface
-----------------------------------

Suppose you have a luban project "helloworld", do ::

 $ cd /path/to/helloworld
 $ luban start

The app will start in a browser

Add a "registration" workflow
=============================

This workflow needs database support. 
The default db engine for luban is sqlalchemy.
Please install sqlalchemy by::

 $ sudo pip install sqlalchemy

.. note::
   Please make sure to use pip for particular python version
   you are using with luban. 
   For example, to work with python 3.2, you may need::

   $ sudo pip-3.2 install sqlalchemy

Back in a terminal,
::

 $ cd /path/to/helloworld
 $ luban workflow add registration

Since the registration needs database support, do:: 

 $ luban db create
 
Now open http://localhost:8080/registration in your browser,
you will see a registration form. Try it out!

More
====

For more details about workflows, see :ref:`"Workflows" <workflow>`

or back to 
:ref:`"Tutorials" <user-tutorials>`

or back to
:ref:`"User Guide" <user-guide>`
