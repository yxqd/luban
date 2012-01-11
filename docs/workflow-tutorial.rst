.. _workflow-tutorial:

Adding a workflow to Your Interface
-----------------------------------

Create a new luban project::

 $ cd /somewhere
 $ luban create workflowdemo
 $ luban start


Add a "registration" workflow
=============================

Now back in a terminal.

This workflow needs database support. 
The default db engine for luban is sqlalchemy.
Please install sqlalchemy by::

 $ sudo pip install sqlalchemy

.. note::
   Please make sure to use pip for particular python version
   you are using with luban. 
   For example, to work with python 3.2, you may need::

   $ sudo pip-3.2 install sqlalchemy

Install "registration" workflow::

 $ cd /path/to/workflowdemo
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
