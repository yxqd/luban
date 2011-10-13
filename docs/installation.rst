.. _installation:

Installation of easy_install or pip
===================================

General instructions
--------------------

python 3
~~~~~~~~

luban 1.0 depends on python 3.1+. Please install python 3.1 or 3.2.

More instructions at http://python.org. (Goto download page of python 3 and 
select the installer for your operating system)


pip
~~~
To install pip, you could first install distribute.
Download distribute from http://pypi.python.org/pypi/distribute#downloads
and expand it and run::

 $ cd distribute-<version>
 $ sudo python3 setup.py install


Then download pip from http://pypi.python.org/pypi/pip#downloads
and expand it and run::

 $ cd pip-<version>
 $ sudo python3 setup.py install

easy_install
~~~~~~~~~~~~

If you already have pip installed, you don't need easy_install.

To install easy_install, download the source tar ball from
http://pypi.python.org/pypi/setuptools#files
and expand it and run::

 $ cd setuptools-<version>
 $ sudo python3 setup.py install



Platform specific instructions
------------------------------

Ubuntu
~~~~~~

For ubuntu 10.04, it is easy to install setuptools::

 $ sudo apt-get install python3-setuptools

Please note that python3 version of easy_install has the command named
easy_install3. So to install luban, do::

 $ sudo easy_install3 luban


Mac OS X
~~~~~~~~

Follow the general instructions above. Just be aware you probably need 
to manually add pip or easy_install to your path::

 $ export PATH=/Library/Frameworks/Python.framework/Versions/<version number>/bin:$PATH


