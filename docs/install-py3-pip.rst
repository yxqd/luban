.. _install-py3-pip:

Installation of pip for python 3
================================

To install pip, you can follow instructions on the pip homepage
(**just make sure you are installing pip for python 3**):
http://www.pip-installer.org/en/latest/installing.html

**Or** you can follow the brief instructions here on how to install
python3 and then pip:

* :ref:`General instructions <install-py3-pip-general>`
* :ref:`Platform-specific instructions <install-py3-pip-platform-specific>`


.. _install-py3-pip-general:

General instructions
--------------------

python 3
~~~~~~~~

luban 1.0 depends on python 3.1+. Please install python 3.1 or 3.2.

More instructions at http://python.org. (Goto download page of python 3 and 
select the installer for your operating system and run it.)



pip
~~~

First, become super user by ::

 $ su

or ::

 $ sudo su

Then install distribute by ::

 $ curl http://python-distribute.org/distribute_setup.py | python3

and then install pip::

 $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python3


.. _install-py3-pip-platform-specific:

Platform specific instructions
------------------------------

Ubuntu
~~~~~~
Under Ubuntu, before installation of pip you may want to install curl,
if it is not yet installed::

 $ sudo apt-get install curl


Mac OS X
~~~~~~~~

Follow the general instructions above. Just be aware you probably need 
to manually add pip to your path::

 $ export PATH=/Library/Frameworks/Python.framework/Versions/<version number>/bin:$PATH


