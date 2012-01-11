.. _history:

History
=======

.. _changes-1.0.1:

Luban 1.0.1
-----------
expected: Jan 15, 2012

Official support of python 2.7.

Experimental:
* python 2.6 support
* "workflows"
* "luban db" command
* "luban paths" command 

.. _changes-1.0.0:

Luban 1.0.0
-----------
Dec 29, 2011

This is the first stable release of luban.

This release presents a luban kernel rewritten in python 3.
By taking advantage of the superior meta-programming capability of
python 3, the new kernel makes it much easier to extend 
the "vocabulary" of the luban "language".

This stable release 
keeps and improves most of the "language features" in earlier
prototype versions such as easy access to element factories and
assignments of actions to event handlers.

The scaffolding for luban projects and extensions were improved
a lot over earlier prototypical versions. It is now much
easier to create, start and stop luban projects.

The layout of a luban project is much simpler and 
therefore easier to understand and work with.

Aokuang is included in this version as a documentation tool
and also a test for luban.
Aokuang shows that good, consistent programming practices
can really lead to much simplified and easy-to-maintain code.

The Gongshuzi prototype is not included in this release.
This release focuses on the "language" core as well as
core infrastructure for luban.

At the end of December 2011, it was decided  that the luban
team will try to back-port luban to support python 2.
It was quickly done and tested with python 2.7 and
there were relatively few changes need to be made for this to
happen due to good design and implementation of the python-3-only luban :)
As a result the 1.0.0 version was shipped with experimental
python 2.7 support. 
However, the super() method of python 2 is much less super than
that of python 3,
so that the luban support for both python 3 and 2 in the long run could be 
difficult if the better super of python 3 were not back-ported
to python 2.7 in the future.
Another thing is that
because of the syntax difference of metaclass in python 2 and 
python 3, some relatively ugly code had to be added 
into places where both multiple inheritance
and metaclass are involved,
in order for
luban to work for both 2 and 3 :(

.. .. _changes-0.2b3:
.. Luban 0.2b3
..
.. Widgets
.. ^^^^^^^
..
.. * downloader


.. _changes-0.2b2:

Luban 0.2b2
-----------
Aug, 2010


This is the second beta release of luban 0.2.
This release has accomodated user feedbacks on using luban
with existing frameworks and IE compatibility.

Working with existing python frameworks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is actually fairly easy to use luban core with any existing
python-based web framework (:ref:`details <webframeworks>`).

In this release, examples for the following web frameworks were added.

 - web.py
 - web.py + google application engine


IE compatibility
^^^^^^^^^^^^^^^^

In the last release, internet explorer was not officially supported.
In this release most of luban work with internet explorer 7 and 8.

There are still problems with some experimental widgets:

 - Code editor


Script to stop luban project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A convenient script to stop a luban project from running was added.
You can now stop a luban project by::

 $ cd <path/to/project>
 $ stop-luban-project.py

or ::

 $ stop-luban-project.py <path/to/project>


.. _changes-0.2b1:

Luban 0.2b1
-----------
June, 2010

This is a release intended for public. So we have focused on
bug fixes, tests, ease of installation.

* Easy install was used to make it easier for users to install
  luban. (:ref:`inistall <installation>`)
* Convenient scripts were created to make it easier for users to
  create, downloand, and run luban projects. (:ref:`download and run
  <download-and-run-luban-examples>` , :ref:`create new <create-luban-project-from-cmdline>`)
* A buildbot+selenium infrastructure was created to auto-test
  luban. Right now there are a few selenium tests for aokuang along
  with unit tests being run every hour when there are changes to
  luban related source trees. (`test site <http://bagua.cacr.caltech.edu:50080/>`_)


New features
^^^^^^^^^^^^
The need of VNF service (http://vnf.caltech.edu) has triggered an
effort to make it easier for users to create forms easily from data
objects. This is done in luban.orm. You can find
:ref:`a tutorial <xyplotter-tutorial>` about that
in the documentation.

Quite a bit efforts went into transforming
`aokuang <http://luban.danse.us/aokuang>`_
into a demo for luban API. 
It now has demos for many of the widgets and illustrate the basic
usages of those widgets. Every demo is accompanied with the code
piece for that demo.
Also the details of widget properties and event handlers are
presented for easy reference.


Some new widgets were introduced:

* dock
* image
* grid
* newsticker(experimental)
* codeviewer(experimental)
* matterbuilder(experimental)
* uploader(experimental)

Some new common events were introduced to all element types:

* oncreate(experimental)
* onkeypress(experimental)

Some new common actions were introduced:

* before
* findDescendentIDs (experimental)


Changes of Interface
^^^^^^^^^^^^^^^^^^^^
The single most important change of API is "page" was renamed "frame".
The old code will still work, however; only a warning will be printed
to
journal log file whenever "page" is used.

The "document" widget got some new properties and event handlers
for expanding and collapsing, and docking and releasing from dock.
The old properties and event handler all work as before.

The "progressbar" widget got a new event handler:

* oncancelled

The "tab" widget got a new event handler:

* onselect

.. tab - onselect, actions enable/disable

.. formselectorfield.notify('changed', ...

The "portletitem" widget got a new event handler:

* onselect

And the "plot2d" widget got two new properties:

* xticks
*  yticks


Misc.
^^^^^
We migrated to use jquery 1.4.


Todo
^^^^
The planning of the new release can be seen in 
`luban roadmap <http://dev.danse.us/trac/luban/roadmap?show=all>`_.


.. _changes-0.2a2:

Luban 0.2a2
-----------
Oct, 2009

Release 0.2a2 had many improvements over 0.2a1.
The main focus of release 0.2a2 was to enrich the UI elements
and element actions, and their corresponding web(javascript)-rendering
mechanisms.

The wxpython (native-python) rendering was also worked on.
Actually we got most widgets implemented, but most of them are
not as full-featured as javascript-rendering. Also not enough efforts
were put into wxpython-rendering to squash bugs yet.
It should be the focus of next release.

A few tests were added. Most widgets now have a testing actor in
tests/aokuang. 

Some efforts were put into IE-compatibility. Luban core is now working
good for IE, but some widgets are still not functioning well enough: 
accordion and treeview.


New features
^^^^^^^^^^^^
Most of the following are referring to the web-rendering part of luban.

One thing worth mentioning is that the dynamic loading of
javascript libraries of UI widgets was implemented. It makes
it much easier to overload the default implementation of UI
widgets in javascript in luban, and to extend luban.

Cookies are now usable as a mechanism to cache the credentials
on the client side. This feature allows users to come back to your 
sites without the need to log in multiple times. This feature
can be disabled too.

Gongshuzi was improved a lot. Users can now launch their
projects as a local website from gongshuzi interface,
and they can also launch their projects as native wxpython applications.
A python code editor is embedded into gongshuzi interface so
that users can use gongshuzi as an integrated UI development
environment.

More actions are now available to manipulate credentials. 
You can now create, update, and delete credentials.
For ease of use, a base class "AuthorizedActor" was 
introduced. All actors inherited from "AuthorizedActor"
will automatically check credentials and all routines there 
will work under credential protection.

Some small improvements were (on web-rendering)

* Implemented a "loading" alert box just to make users a bit more comfortable
  when page is loading.
* Implemented a simple "error report" dialog. 

New UI Elements:

* FormCheckBox
* FormRadioBox
* Plot2D

(The following elements are undocumented yet)

* HtmlDocument
* ReStructuredTextDocument
* ProgressBar
* CodeEditor

All UI elements have a javascript renderer. 

Some of UI elements have a wx python renderer.
The new additions in 0.2a2 were:

* Link
* AppMenuBar
* Accordion
* TreeView
* Table

New actions:

* show/hide
* enable/disable
* getAttr/setAttr


Changes of interface
^^^^^^^^^^^^^^^^^^^^

ui elements
"""""""""""
* All elements now have the attribute "hidden".

actions
"""""""
Element-specific actions now have a similar syntax::

 >>> selector.<elementtype>(<actionname>, **<actionparameters>)

Following actions were changed accordingly (the old interfaces still work
but generate DeprecationWarning):

* selector.showError --> selector.formfield('showError', message=...)
* selector.setTreeViewRoot --> selector.treeview('setRoot', root=...)
* selector.addTreeViewBranch --> selector.treeview('addBranch', referencenode=..., newnode=..., position=...)
* selector.removeTreeViewNode --> selector.treeview('removeNode', node=...)

For more details of new interface, please refer to 
:ref:`API <API>`.

css classes
"""""""""""
The css classes of some luban-generated html elements were changed to have
more consistent names. But the old class names are also available in this release
for backward compatibility and will phase out in future releases

Portlet

* visualPadding --> luban-portlet-padding
* portlet --> luban-portlet
* portletBody --> luban-portlet-body
* portletitem-container --> luban-portletitem-container
* portletContent --> luban-portletitem-content
* navItem --> luban-porletitem
* navItemIcon --> luban-portletitem-icon
* navItemText --> luban-portletitem-text

Form fields

* formfield --> luban-formfield
* formfieldHelp -> help



Luban 0.2a1
-----------
Aug, 2009

Release 0.2a1 was a proof-of-concept prototype. It demonstrates that we can
describe UI elements and UI actions using a generic langauge and translate
that language into appropriate code. 

It establishes the architecture of Luban, and lays out a structure that is extensible.

It implements some basic widgets, actions, and web rendering of most of widgets
and wx rendering of some of widgets.

The wigets and actions in 0.2a1 are:

Widgets:
 * Page
 * Document
 * Splitter

  * splitsection

 * Portlet

  * portletitem

 * Toolbar
 * Form

  * textfield
  * passwordfield
  * textarea
  * selector
  * submitbutton

 * AppMenuBar

  * menu
  * menuitem

 * TreeView

  * branch
  * leaf

 * Accordion

  * accordionsection

 * Tabs

  * tab

 * Paragraph
 * Link
 * Button
 * Credential
 * Table

Actions:
 * select
 * load, submit, notify
 * element.

  * empty, replaceContent, append
  * destroy
  * setAttr
  * addClass, removeClass

 * removeCredential
 * alert

It contains a preliminary version of gongshuzi, the UI builder, and demonstrates
the rich interactivities that can be achieved by using luban.


Migrate from Luban 0.2a1 pre-release to Luban 0.2a1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A couple of developers have used the pre-released luban 0.2a1. 
The pre-released luban 0.2a1 was created on top of pyre/opal and has
inherited many interfaces and structures from pyre/opal.
Before it is released, several changes have been made to luban in order
to

 * make the directory structure more clean/slim
 * make it easier to start luban applications
 * simplify some interfaces


Directory structure
"""""""""""""""""""
First off, most of the changes are optional (except the last item below about content/visuals),
but these changes, we believe, can make your directory cleaner and slimer.

NOTE: there is a very useful script in luban 0.2a1: create-luban-project.py. Just run ::

  $ create-luban-project.py --name=<new project name>

you will get a new project with a good directory structure

In pre-release, luban was using a directory structure similar to that of opal.
Several changes have been made to simplify the directory structure:

 * <luban-project>/applications/WebApplication.py: removed. This file is not necessary anymore unless there are really special things need to be done to extend the default web (and/or wx) application. Just use the default wxmain.py and webmain.py should work for most common cases.
 * bin/\*: most of files here are no longer needed. Services idd and journald were moved to become luban "system" binaries. Users only need to start default luban services (journald and idd) by using script "start-luban-services.sh". If there are any project-specific services (daemons), or other applications, you can put them here.
 * cgi-bin/\*: most of files here are no longer needed. In case of you are using the "development simple http server", i.e. SimpleHttpServer.py, to test your application, you will need one fixed file "main.py", which is available if you use script create-luban-project.py to create your project
 * config/\*: many of the files here should be removed, such as idd related files, ipa related files. They are now handled by script "start-luban-services.sh" and are generated by default in /tmp/luban-services
 * content: For opal projects, content usually have several subdirectories such as actors, pages, portlets etc. In luban-0.2a1, it is required that all components for "visuals" (pages, portlets are all visuals) are under the directory "visuals". What you could do is to move all contents in the directories "pages", "portlets", etc, into one single directory "visuals". This we believe makes the directory structure easier to understand, because all "pages", "portlets" are just visuals. If you want to differentiate those different types of visuals, you could create subdirectories in the "visuals" directory:

   * visuals

    * portlets
    * pages

   and the way to retrieve visual from a component named "navigation.odb" in subdir "portlets" (for example) is ::

     director.retrieveVisual("portlets/navigation")

   Also, another thing that happened to the "content" directory is that there is an "images" directory added. 
   It is actually moved over here from "html/images". The thinking is that the directory "images" is going to be used by both web and wx applications, and should not be limited in the "html" directory. The "images" entry in the "html" directory is now actually a symbolic link.


Start luban applications
""""""""""""""""""""""""

Luban applications in 0.2a1 release is easier to start than those in 0.2a1 pre-release. 
In 0.2a1, starting a luban application usually only consists of 2 steps:

  * run start-luban-services.sh
  * start simple http server: SimpleHttpServer.py under the exported html directory.

As explained partially in the previous section, some "system-wide" daemons are
started by the script start-luban-services.sh.


Interface change
""""""""""""""""

Some minor changes to interface happened:

 * director.retrievePage is gone. Page sounds too specific. A more generic name, "visual" 
   replaces "page". So director.retrieveVisual should be used in place of director.retrievePage
   or director.retrievePortlet,
   and all odb files that generating visuals should replace ::

    def page(...): ...

   or ::

    def portlet(...): ...

   by ::

    def visual(...): ...

 * Splitter. Splitter usually has an attribute "direction". We decided to change that to "orientation", and direction=vertical in pre-release actually means orientation=horizontal.



Luban 0.1
---------
2007

Luban 0.1 allows users to create wx user interface using a structured document, like an xml file. 
It is not released to the public but is used by the HistogramGUI application.


