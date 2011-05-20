.. _installation:

Installation
============


The short version
-----------------

.. note::
   If you have an early installation of the development version of
   luban 0.2, please remove it by::
   
   $ rm -rf </path/to/luban>

Install it with easy_install ::
 
 $ sudo easy_install -U luban==0.2dev


or, 

get luban from the `Python Package Index
<http://pypi.python.org/pypi/luban/0.2dev>`_, expand it and run ::

 $ sudo python setup.py install
    

Or if you need :ref:`more details <installbyeasyinstall>`:


.. _installbyeasyinstall:

Install luban using easy_install
--------------------------------

Prerequisites
^^^^^^^^^^^^^

Luban is installable on unix/linux platforms, as well as Mac OS X
operating systems.
Luban has not been tested in windows system.

Please make sure your system has the following software installed:

#. `Python <http://www.python.org>`_ (version 2.x)
#. `setuptools <http://pypi.python.org/pypi/setuptools>`_. 
#. (optional, only needed if you want to run native wx application) `wx python <http://www.wxpython.org/>`_
#. (optional, only needed if you want to use the experimental orm feature) `numpy <http://numpy.org/>`_


Platform-specific instructions
""""""""""""""""""""""""""""""
Mac OS X 10.5.x and 10.6.x
''''''''''''''''''''''''''
* python:
  Mac OSX comes with python pre-installed. You can also install the
  more recent python version from `python website <www.python.org>`_.
* setuptools:
  Following instructions are copied from setuptools website

 #. Download the appropriate egg for your version of Python (e.g. setuptools-0.6c11-py2.6.egg). Do NOT rename it.
 #. Run it as if it were a shell script, e.g. ::

     $ sh setuptools-0.6c11-py2.6.egg

    Setuptools will install itself using the matching version of Python (e.g. python2.6), and will place the easy_install executable in the default location for installing Python scripts (as determined by the standard distutils configuration files, or by the Python installation).

* (optional) wxpython:
  Download and install  appropriate wxpython binary from 
  `wxpython website <http://www.wxpython.org>`_: 
  `wxpython 2.8.10.1 Mac Universal Disk Image <http://downloads.sourceforge.net/wxpython/wxPython2.8-osx-unicode-2.8.10.1-universal-py2.6.dmg>`_

Ubuntu 8.x and 9.x
''''''''''''''''''
* python
  Ubuntu 8.x and 9.x are preinstalled with python.

* setuptools
 We can intall setuptools by::

  $ sudo apt-get install python-setuptools

* (optional) wxpython: ::

  $ sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n


Install
^^^^^^^

Run ::

 $ sudo easy_install luban==0.2dev



To start playing with luban, please read :ref:`tutorials <Tutorials>`.


