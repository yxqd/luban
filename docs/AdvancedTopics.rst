.. _advanced-topics:

Advanced topics
===============

Luban applications and services
-------------------------------



Common Services
^^^^^^^^^^^^^^^

Luban applications need some common services to function correctly.
All services are pyre daemons.
To start a daemon, do ::

  $ <daemon> --config=<list of config directories> --home=<home directory>

For example, start an idd (global unique id generator) daemon ::

  $ idd.py --config=idd-config --home=idd-home

There is a convenient script to start all luban services ::

  $ start-luban-services.sh

By default, the "home" directory for the started services is ::

  /tmp/luban-services

You can change the "home" directory by ::

  $ start-luban-services.sh --home=<home of services>



Application-specific services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some applications need additional services to work. For example, the authentication
daemon, ipa, is needed for any application that grant users access by somehow checking
user's identity.

To start those services, you first need to change your working directory ::

  $ cd $EXPORT_ROOT/<lubanapp>/bin

where <lubanapp> is the name of the luban application.
And then you can start the services by ::

  $ ./startservices.sh


Main applications
^^^^^^^^^^^^^^^^^

WX application
!!!!!!!!!!!!!!
The support of WX interface rendering is only partially supported at this moment.
So the following instructions may not work for some luban applications.

You are now ready to start the main applications. To start the wx application ::

  $ cd $EXPORT_ROOT/<lubanapp>/bin
  $ wxmain.py


Web application
!!!!!!!!!!!!!!!

To start the web application using the simple http server ::
  
  $ cd $EXPORT_ROOT/<lubanapp>/html
  $ SimpleHttpServer.py


Now take a look at the configuration file of the simple http server ::

  $ cd $EXPORT_ROOT/<lubanapp>/config
  $ vi SimpleHttpServer.pml

and note the port number. Open the following address in your browser ::

  http://localhost:<port number>/cgi-bin/main.py





Customize your web application
------------------------------


Cookie
^^^^^^
You can enable cookie support for better user experiences. 
Cookie is used by luban to cache user's authentication token.
To enable cookie support for your web application, modify the file ::

    config/web-weaver.pml

and add the following::

	<property name="cookie-path">/cgi-bin/</property>
	<property name="use-cookie">on</property>

You have to set "use-cookie" to "on" or "true" or "yes" to enable the cookie support;
the property "cookie-path" should be set to the path of your web application.
For example, if you web application is hosted at ::

  http://my.website.org/cgi-bin/myapp/main.cgi

You should set "cookie-path" to ::

  /cgi-bin/myapp/

You can always set "cookie-path" to ::

  /

if you are lazy, or if all your web applications in this domain "http://my.website.org" share the same authentication service.


Look and feel
^^^^^^^^^^^^^
Luban assign special class names to the html elements it created for luban widgets, 
so that you can customize the look and feel of your web application using 
normal css tricks.

The best way to do this customization, in my humble opinion, is to use firebug to investigate
the html elements you need to customize and tweak the css settings with firebug.


Form fields
!!!!!!!!!!!

All luban form fields (FormTextField, FormPasswordField, etc) rendered has class::

  luban-<field-type-name>

For example, a FormTextField is rendered as a "div" that has a class ::

  luban-formtextfield

So to select container divs of all FormTextFields, do ::

  .luban-formtextfield {
  }

To select "input" tag in the container div for a FormTextFields, do ::

  .luban-formtextfield  input {
  }


inline and block
""""""""""""""""
The default css for luban puts the label of the form field and the form field itself in different lines.
You could use "inline" or "block" to put them in the same line.


