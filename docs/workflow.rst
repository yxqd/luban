.. _workflow:

Workflow scaffolding
--------------------

You can manage workflows using the "luban workflow" command.
Try the following::

 $ cd <luban-project>
 $ luban workflow
 $ luban workflow add

To add a workflow::

 $ luban workflow add <name-of-workflow>

For example, to install the "registration" workflow::

 $ luban workflow add registration

After install a workflow example, make sure to read and maybe
edit the following file::

 <project>/deployments/<deployment>/luban_app_config.py

which contains configurations of your luban application.

Then you can run a demo of this workflow, usually at
http://localhost:8080/<workflow-name>


In the next sections, we explain workflow examples one by one.

registration
============

Configurations
""""""""""""""

* db: database configuration

.. note::
 Reminder: configurations are in::

  <project>/deployments/<deployment>/luban_app_config.py

Demo
""""

http://localhost:8080/registration


Workflow customization
""""""""""""""""""""""

 >>> Workflow.models_factory.Base = <base class of db models>
 >>> Workflow.actor_factory.hashfunc = <hash function for password>


login
=====


Configurations
""""""""""""""

* db: database configuration


Demo
""""

http://localhost:8080/login


Workflow customization
""""""""""""""""""""""

 >>> Workflow.models_factory.Base = <base class of db models>
 >>> Workflow.actor_factory.hashfunc = <hash function for password>


feedback
========

Configurations
""""""""""""""

This demo workflow by default assumes you want to use gmail smtp server
to send the feedback email to your site's feedback email address.
It thus needs information about your gmail account,
and also the email address for receiving feedbacks.

* feedback_recipient
* gmail_account


Demo
""""

http://localhost:8080/feedback?email=user@company.com


Workflow customization
""""""""""""""""""""""

 >>> Workflow.actor_factory.smtp = <smtp instance>


