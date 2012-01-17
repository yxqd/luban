.. _developer-guide:

Luban Developer Guide
=====================

Send an email with ssh public key and your ip range to team@lubanui.org.
After your public key is set up correctly, you can
then do the following.

Install prerequisites::

 $ sudo apt-get install yui-compressor bzr python3 python-pip
 $ sudo pip install beim sqlalchemy cherrypy sphinx


Establish development directory and build::

 $ mkdir -p dv
 $ cd dv
 $ bzr whoami "firstname lastname <email>"
 $ bzr init-repo .
 $ bzr branch bzr+ssh://bzr@bagua.cacr.caltech.edu/luban/releaser luban-releaser
 $ cd luban-releaser
 $ ./getsrc.py
 $ ./create-py2-link
 $ ./build
 
Directories:

* src: sources
 * luban: the luban sources
 * merlin: little (experimental) builder

* EXPORT: products to export
 * bin: executables. should be added to $PATH
 * packages: python packages. should be added to $PYTHONPATH
 * share: documentation etc
 * (other directories): example luban projects, including aokuangs.

bin/envs.sh is a shell script that, when sourced, establish 
PATH and PYTHONPATH etc.

