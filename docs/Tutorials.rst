.. _tutorials:

Tutorials
=========

If you have not done so, please 
:ref:`install <installation>`
luban before you trying the following tutorials.


.. _download-and-run-luban-examples:

Download and run luban examples
-------------------------------

Convenient scripts come with luban installation so you can easily download and run luban examples.
For example, if you want to install and run luban example project "aokuang", run ::

    $ cd <somewhere-in-your-home-directory>
    $ download-luban-project.py aokuang
    $ start-luban-project.py aokuang

A browser window will be opened to show the web application aokuang.

Available example projects are:

* aokuang (`live demo <http://luban.danse.us/aokuang>`_)
* plotfx (`live demo <http://luban.danse.us/plotfx>`_)
* jazzclub (`live demo <http://luban.danse.us/jazzclub>`_)
* gongshuzi (:ref:`documentation <gongshuzichapter>`, `demo site <http://luban.danse.us/gongshuzi>`_)

To stop a luban project from running::

   $ stop-luban-project.py <path-to-the-project>


.. _create-luban-project-from-cmdline:

Create my first luban application from command line
---------------------------------------------------

.. note::
   You could create and manage your luban project visually using application
   :ref:`Gongshuzi <gongshuzichapter>`, which is still experimental,
   however.


Luban project creator script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can create a template luban project by using the script "create-luban-project.py".
To create your own luban application, do the following ::

 $ cd /anywhere/you/like
 $ create-luban-project.py

This will create a project named "helloworld". To create a luban project with a name
of your choice, do ::

 $ create-luban-project.py <project name>

Now you can start your project, ::

 $ start-luban-project.py helloworld

or ::

 $ start-luban-project.py <project name>

Now a browser window should be open with your 
`first luban web application <http://localhost:8801/cgi-bin/main.py>`_
.
You should see a page that is titled "Hello world".

You can also see the wx application running by ::

 $ cd /path/to/helloworld/bin
 $ wxmain


Directory structure
^^^^^^^^^^^^^^^^^^^
Now let us take a look at the structure of our luban project. 
There are a few subdirectories in directory "helloworld".

* config: configuration files. Most of them are xml files (ending with .pml). They are useful for fine tune the behavior of various components that constitute your luban application.
* bin: executables specific for this application. For example, some applications need intialization scripts or services (daemons) to be run before the application can work correctly.
* log: logging files. You will look for debugging information here.
* html, cgi-bin: specific for web application. You can fine tune your css style sheets to improve the visual appearance of your interface here.
* helloworld: the python source tree for the helloworld project. This will, for example, contain data models for your application.
* content: this is the main directory that gives your luban user interface functionalities. 

At your first attempt to build a luban application, only the directory "content"
need to be touched.

In directory "content", there are following subdirectories:

* images: images to be used in your user interface
* components: the user interface components

 * actors: components that handles user interactions
 * visuals: components that build the ui elements/hierarchies


Actor
^^^^^

Actor is the component that responds to user requests. In web applications, a method of an actor can be
accessed through a url that looks like ::

  http://web.site/main.py?actor=<actor_name>&routine=<routine_name>

For example, ::

  http://web.site/main.py?actor=helloworld&routine=default

will call the method "default" of actor "helloworld". 

In WX applications, a command line ::

  $ wxmain.py --actor=helloworld --routine=default

will call the same method.

Now let us look at our helloworld actor (which can be found in
helloworld/content/components/actors/helloworld.odb) ::

  def actor():
      from luban.components.Actor import Actor as base
      class Actor(base):
	  def default(self, director):
	      return director.retrieveVisual('helloworld')
      return Actor('helloworld')

An actor file must have extension ".odb", and it is a python source file.
It must define a method "actor", which takes no arguments and returns
an instance of a class derived from luban.component.Actor.Actor.

Any method of the derived Actor class that takes a "director" argument
can be invoked through a web link or a python command line.
In this helloworld example, the default method just simply returns a 
visual::

        return director.retrieveVisual('helloworld')

Please refer to :ref:`retrieveVisual <retrieveVisual>`.


Visual
^^^^^^
This the code for the "helloworld" visual 
(helloworld/content/components/visuals/helloworld.odb)::

  def visual(director):
      import luban.content
      frame = luban.content.frame(title='test frame')
      
      doc = frame.document(title='Hello world!')
      doc.paragraph().text = ['This is a test.']
      
      return frame

It defines a method "visual" which takes an argument "director".
The body of the "visual method creates a "frame", and 
then adds a "document" inside the frame, and then adds
a "paragraph" inside the document.


Conclusive remark
^^^^^^^^^^^^^^^^^

In this tutorial, we go through the procedure of creating one luban
application and describes the main components for this simple
luban application, and introduces concepts like "actors", "visuals".

In the next tutorial, we are going to build a more complex 
application.



Adding a login form
-------------------

In this tutorial we will add a login form step by step. 

.. note::
   It is actually a quite straighforward procedure to build a form in
   luban,
   but it may still look
   tedious. In that case, there is a way in luban to make
   form creation and handling easy. Please refer to
   :ref:`x-y plotter tutorial <xyplotter-tutorial>` for an example of that.
   But I would suggest that you read this tutorial patiently since it
   goes through some important concepts of luban such as actions
   and event handlers.


Now, go to your "helloworld" directory::

  $ cd /path/to/helloworld

As described in the last section, it has following subdirectories which are the main ones to touch ::

  content/components/actors
  content/components/visuals


The form
^^^^^^^^

We will first create the form in a file called login.odb inside the "visuals" directory ::

  # -*- Python -*-
  # helloworld/content/components/visuals/login.odb

  def visual(director):
      import luban.content
      document = luban.content.document(title = 'Login')
      
      # build the login form
      form = document.form(id='login-form')

      username = form.text(
	  name='username', label='Username', value='', id='login-username-input')

      password = form.password(
	  name='password', label='Password', value='', id='login-password-input')

      submit = form.submitbutton(label="login")

      # action when form is submitted
      from luban.content import select
      form.onsubmit = select(element=form).submit(
	  actor = 'login',
	  routine = 'verify',
	  )

      p = form.paragraph()
      p.text = [
	  'When you are done, please logout or exit your browser'
	  ]
      return document

    
and then we create an actor in the actors directory called login.odb to load this visual and show it ::

  # -*- Python -*-
  # helloworld/content/components/actors/login.odb

  from luban.components.Actor import Actor

  class Login(Actor):

      def default(self, director):
          import luban.content
          frame = luban.content.frame(title='login')
	  
	  doc = director.retrieveVisual('login')
          frame.add(doc)

	  return frame

      def __init__(self, name=None):
          if name is None:
              name = 'login'
          super(Login, self).__init__(name)
          return

  def actor():
      return Login()

With these two files, you should be able to see your login form in your browser:
`the login form <http://localhost:8801/cgi-bin/main.py?actor=login>`_ .
But the form does not do anything for you just yet. 

The "onsubmit" event handler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To let the user's mouse-click on the submit button to have some effect,
let us change the "login" actor to::

  # -*- Python -*-
  # helloworld/content/components/actors/login.odb

  from luban.content import alert, select

  from luban.components.Actor import Actor

  class Login(Actor):

      def default(self, director):
          import luban.content
          frame = luban.content.frame(title='login')

          doc = director.retrieveVisual('login')
          frame.add(doc)

          form = doc.find(id="login-form")
          form.onsubmit = alert('form submitted')
          return frame

      def __init__(self, name=None):
          if name is None:
              name = 'login'
          super(Login, self).__init__(name)
          return

  def actor():
      return Login()

If you 
`try it out <http://localhost:8801/cgi-bin/main.py?actor=login>`_ 
now, clicking the submit button will give you an alert.
This line::

          form.onsubmit = alert('form submitted')

tells luban that when this form is submitted, do an action::

     alert('form submitted')

This action is to show an alert message box.

Calling the actor when submit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To really submit the form information for the controller to process, we need to make slight
changes to the line::

          form.onsubmit = alert('form submitted')

and make it ::

          form.onsubmit = select(id='login-form').submit(actor='login', routine='verify')

This tells luban that for the form submission event, the action is

 1. select the UI element whose id is "login-form", which selects the form
 2. submit the information in the form to the actor "login" and call method "verify"
 3. run the action(s) returned

So, let us change the login actor to::

  # -*- Python -*-
  # helloworld/content/components/actors/login.odb

  from luban.content import alert, select

  from luban.components.Actor import Actor

  class Login(Actor):

      def default(self, director):
          import luban.content
          frame = luban.content.frame(title='login')

          doc = director.retrieveVisual('login')
          frame.add(doc)

          form = doc.find(id="login-form")
          form.onsubmit =  select(id='login-form').submit(actor='login', routine='verify')
          return frame

      def verify(self, director):
          return alert('form submitted')

      def __init__(self, name=None):
          if name is None:
              name = 'login'
          super(Login, self).__init__(name)
          return

  def actor():
      return Login()


If you 
`try it out <http://localhost:8801/cgi-bin/main.py?actor=login>`_ 
now, clicking the submit button will give you an alert again.
But please note this is different from the previous step because
in this example, the "submit" event actually triggers a trip
to the controller which calls the method "verify" of actor "login"
and the returned action(s) are taken.


Error checking
^^^^^^^^^^^^^^

Now we want to check errors in the form when it is submitted,
we need to expand the "verify" method and this is the new actor ::

  # -*- Python -*-
  # helloworld/content/components/actors/login.odb

  from luban.content import alert, select

  from luban.components.Actor import Actor

  class Login(Actor):

      class Inventory(Actor.Inventory):

          import pyre.inventory
          username = pyre.inventory.str('username')
          password = pyre.inventory.str('password')


      def default(self, director):
          import luban.content
          frame = luban.content.frame(title='login')

          doc = director.retrieveVisual('login')
          frame.add(doc)

          form = doc.find(id="login-form")
          form.onsubmit =  select(id='login-form').submit(actor='login', routine='verify')
          return frame

      def verify(self, director):
          errors = {}

          username = self.inventory.username
          if not username:
              errors['username'] = 'Username cannot be empty'

          password = self.inventory.password
          if not password:
              errors['password'] = 'Password cannot be empty'

          if errors:
               return self.showErrors(director, errors=errors)

	  raise NotImplementedError

      def showErrors(self, director, errors=None):
          from luban.content import select
          return [
              select(id='login-%s-input' % name).showError(text)
              for name, text in errors.iteritems()
              ]

      def __init__(self, name=None):
          if name is None:
              name = 'login'
          super(Login, self).__init__(name)
          return


  def actor():
      return Login()


Further reading
^^^^^^^^^^^^^^^
For a complete example of a login form, please refer to the Jazz Club example.
This is `the source code of the login actor for Jazzclub example
<http://dev.danse.us/trac/luban/browser/trunk/examples/jazzclub/content/components/actors/base/login.odb>`_. 




.. _xyplotter-tutorial:

Create a simple function plotter web service in few minutes
-----------------------------------------------------------

The goal of this tutorial is to create a web service to plot 
a function y=f(x) configurable by user.


start up
^^^^^^^^

Let us start by create a new luban project::

 $ cd <somewhere>
 $ create-luban-project.py plotfx

This creates a directory "plotfx" and several sub directories.

You could see it running by ::

 $ start-luban-project.py plotfx

A browser should pop up with url http://localhost:8801/cgi-bin/main.py


Sin Function
^^^^^^^^^^^^
Now let us create a data object represent the function y=sin(a*x+b).
Please use your favorite editor to create python source 
plotfx/plotfx/Sin.py::

 import numpy
 
 class Sin(object):
 
   a = 1.0
   b = 0.0
 
   def __call__(self, x):
       a = self.a
       b = self.b
       return numpy.sin(a*x+b)

It has two parameters a and b, and a method __call__ to compute ::

  y = f(x) = sin(a*x+b)


orm for sin function
^^^^^^^^^^^^^^^^^^^^

Here, we use the magic of orm in luban to turn the data object to a
form. Please run ::

 mkdir -p plotfx/content/components/actors/orm

and create a file
plotfx/content/components/actors/orm/sin.odb::

 from plotfx.Sin import Sin
 import luban.orm
 Actor = luban.orm.object2actor(Sin, needauthorization=False)
 def actor(): return Actor('orm/sin')

Please point your browser to
http://localhost:8801/cgi-bin/main.py?actor=orm/sin&routine=debug_edit
, and you will see a form was created for the Sin data object.

.. image:: /images/plotfx-tut/sin-orm-form.png
   :width: 250px

And the form already knows that the input value has to be floating
point numbers: if you type in something other than that and submit,
an alert will show up.

.. image:: /images/plotfx-tut/sin-orm-form-b-must-be-float.png
   :width: 250px



CurveComputation
^^^^^^^^^^^^^^^^

In order to plot a curve of the user specified function, we need a
curve computation that takes a function and a specification of the x
axis, and generates y points for each x points.


Please create file plotfx/plotfx/CurveComputation.py::

 import numpy
  
 from Sin import Sin
 
 class CurveComputation(object):
 
     function = Sin()
 
     xmin = 0.0
     xmax = 10
     xstep = 0.1
 
 
     def __call__(self):
         xmin = self.xmin
         xmax = self.xmax
         xstep = self.xstep
         x = numpy.arange(xmin, xmax, xstep)
         f = self.function
         return f(x)

and file
plotfx/content/components/actors/orm/curvecomputation.odb::

 from plotfx.CurveComputation import CurveComputation
 import luban.orm 
 Actor = luban.orm.object2actor(CurveComputation, needauthorization=False)
 def actor(): return Actor('orm/curvecomputation')

Please point your browser to
http://localhost:8801/cgi-bin/main.py?actor=orm/curvecomputation&routine=debug_edit
you will see a form in which you can edit a computation, including the
sin function:

.. image:: /images/plotfx-tut/curvecomputation-form.png
   :width: 280px


Main actor
^^^^^^^^^^

We can now edit the main actor 
plotfx/content/components/actors/plotfx.odb
to be::

 # -*- python -*-
 
 from luban.content import select, load, alert
 import luban.content as lc
 
 
 from luban.components.Actor import Actor as base
 
 class Actor(base):
 
 
     class Inventory(base.Inventory):
 
         import pyre.inventory
         
         id = pyre.inventory.str('id')
         
         pass
        
        
     def default(self, director):
         "this is the main routine of this main actor"
         # create a new computation
         comp = CurveComputation()
         # save it to db
         orm = director.clerk.orm
         orm.save(comp)
         id = orm(comp).id
         # load skeleton
         frame = self._createSkeleton()
         # fill the input container with the form of the computation
         inputcontainer = frame.find(id='input-container')
         inputcontainer.oncreate = select(element=inputcontainer).replaceContent(
             load(actor='orm/curvecomputation', routine='edit', id=id)
             )
         # action of run button: create plot and add it to the output container
         runbutton = frame.find(id='run-button')
         runbutton.onclick = select(id='output-container').replaceContent(
             load(actor=self.name, routine='createPlot', id=id)
             )
         return frame

 
     def createPlot(self, director):
         # load computation from db
         id = self.inventory.id
         orm = director.clerk.orm
         comp = orm.load(CurveComputation, id)

         # run the computation to get x, y
         x, y = comp()
         
         # create plot
         plot = lc.plot2d()
         plot.curve(x=list(x), y=list(y))
         
         return plot
 
 
     def _createSkeleton(self):
         "create the skeleton of the main interface"
         # the frame
         frame = lc.frame()
         # a splitter to split the space to left, middle, right
         sp = lc.splitter(orientation='horizontal')
         frame.add(sp)
         # left: input
         left = sp.section(Class='align-top')
         left.document(title='Input', id='input-container')
         # middle: run button
         middle = sp.section()
         button = lc.button(id='run-button', label='plot')
         middle.add(button)
         # right: output
         right = sp.section(Class='align-top')
         right.document(title='Output', id='output-container')        
 
         return frame
      
         
 from plotfx.CurveComputation import CurveComputation
 
 
 def actor():
     return Actor("plotfx")


Then, if you point your browser to
http://localhost:8801/cgi-bin/main.py
you will see the web service. Click the "plot" button to see a plot of
sin wave:

.. image:: /images/plotfx-tut/application-with-plot.png
   :width: 420px

You can change the parameters of the function and the x axis, and
click the "save" buttons for the function and the computation, and
click "plot" button again, you will see an updated plot. For example,
the following one:

.. image:: /images/plotfx-tut/application-with-plot-2.png
   :width: 420px


Support more types of functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can make this application more flexible; it should be able to plot
various kinds of functions. To do this we first define an abstract
interface for functors (plotfx/plotfx/Functor.py)::

 class Functor(object):
 
   def __call__(self, x):
       raise NotImplementedError


And we modify the Sin functor to inherit from Functor 
(plotfx/plotfx/Sin.py)::

 import numpy
 
 from Functor import Functor
 class Sin(Functor):
 
   a = 1.0
   b = 0.0
 
   def __call__(self, x):
       a = self.a
       b = self.b
       return numpy.sin(a*x+b)


and we create a new functor "exponential"
(plotfx/plotfx/Exponential.py)::

 import numpy
 
 from Functor import Functor
 class Exponential(Functor):
 
   c = 1.0
 
   def __call__(self, x):
       c = self.c
       return numpy.exp(c*x)

and create a orm actor for the new functor "exponential"
at plotfx/content/components/actors/orm/exponential.odb::

 from plotfx.Exponential import Exponential
 import luban.orm
 Actor = luban.orm.object2actor(Exponential, needauthorization=False)
 def actor(): return Actor('orm/exponential')


Then we modify the CurveComputation class
(plotfx/plotfx/CurveComputation.py)
to ::

 import numpy
 
 from Functor import Functor
 
 
 from Sin import Sin
 from Exponential import Exponential
 functor_types = [Sin, Exponential]
 
 
 from dsaw.model.Inventory import Inventory as InvBase
 class CurveComputation(object):
 
     function = None
     xmin = 0.0
     xmax = 10
     xstep = 0.1
 
     class Inventory(InvBase):
         
         function = InvBase.d.reference(
             name='function',
             targettype=None, targettypes=functor_types,
             owned = 1)
 
         xmin = InvBase.d.float(name='xmin', default=0.)
         xmax = InvBase.d.float(name='xmax', default=10.)
         xstep = InvBase.d.float(name='xstep', default=0.1)
 
 
     def __call__(self):
         xmin = self.xmin
         xmax = self.xmax
         xstep = self.xstep
         x = numpy.arange(xmin, xmax, xstep)
         f = self.function
         return x, f(x)


Here we introduce descriptors to better describe the
data members of CurveComputation. 
Especially important is the descriptor of "function" reference::

         function = InvBase.d.reference(
             name='function',
             targettype=None, targettypes=functor_types,
             owned = 1)

It tells luban that the reference "function" is owned by a
CurveComputation object.
The reference is polymorphic and the allowed types are
the list "functor_types".

Now we are almost ready to see the more powerful application
running. Before that we need to remove the old database file
since the reference "function" has changed from a non-polymorphic
one to a polymorphic one::

  $ rm plotfx/content/db.sqlite

Now we can point our browser to
http://localhost:8801/cgi-bin/main.py?actor=plotfx
again.
In the Function section you can now change the type of the function
you want to plot, and change parameters, and plot it:

.. image:: /images/plotfx-tut/application-with-exp(x)plot.png 
   :width: 480px
 

Wrap my favorite javascript library (widget) and use it in luban
----------------------------------------------------------------
Say you want to wrap a widget in luban. Things need to be done are

1. create a python API for your widget
2. implement a javascript wrapper of the widget 
3. register this widget with luban

Here we use a simple example to illustrate these steps.

In this example we will create a simple widget that 
plot a plot of x-y curve(s) using `protovis <http://vis.stanford.edu/protovis/>`_.


python representation of the widget
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A widget has properties, events, and actions. In this simple example,
we
will only consider the properties of a widget. Here is the code piece 
to define the widget API::

    from luban.content.Element import Element

    class Chart(Element):

        simple_description = 'Chart'
        full_description = ''
	
        # list all subelements and properties here
	#
	# a subelement
        curves = Element.descriptors.referenceSet(name='curves')
        curves.tip = 'The x-y curves to display'
        # ... more sub elements if necessary ...
	#
	# a property
        caption = Element.descriptors.str(name='caption')
        caption.tip = 'caption of the chart'
	# ... more properties ...

        abstract = False   # this element is not an abstract one
        experimental = True  # this is an experimental element

	# method for visitor. always needed	
        def identify(self, visitor):
            return visitor.onChart(self)

	# convenient method to create subelements
        def curve(self, **kwds):
            curve = ChartCurve(**kwds)
            self.curves.append(curve)
            return

    # define subelements
    class ChartCurve(Element):
    
         ...

`Code <http://dev.danse.us/trac/luban/browser/trunk/examples/chart/chart/content/Chart.py>`_

Javascript wrapper
^^^^^^^^^^^^^^^^^^

It is necessary to write a piece of javascript code to wrap the
javascript library so that luban knows how to handle the new
widget::

 (function(luban, $) {

  // aliases
  var ef = luban.elementFactory;
  ...

  // documentmill handler. must define dmp.on<element name>.
  // usually, just assign it to the default handler dmp._onElement is
  // good enough
  var dmp = luban.documentmill.prototype;
  dmp.onchart = dmp._onElement;


  //  factory method. This is the method to construct html element(s)
  //  for the widget out of the properties of the widget.
  ef.chart = function(kwds, docmill, parent) {

    // kwds: the dictionary that contains all information to construct
    //         the new widget
    // docmill: luban element -> html element renderer
    // parent: parent element
    var div = tag('div', {'id': kwds.id});
    div.addClass('luban-chart');
    ...
   
    var ret = div.lubanElement('chart');
    if (parent) {parent.add(ret);}

    ...
    return ret;
  };
  //  js object of the luban element. this is in the same form for
  //  every widget types.
  widgets.chart = function(elem) {
    this.super1 = widgets.base;
    this.super1(elem);
  };
  widgets.chart.prototype = new widgets.base ();
  
  ...
  // implementation details
  ...
 })(luban, jQuery);

`code <http://dev.danse.us/trac/luban/browser/trunk/examples/chart/html/javascripts/chart.js>`_

register this widget with luban
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The idea here is that you will need to let luban know the python
(sub)package that contains definitions of new luban widget(s).
This is done by overloading the web-weaver-library component.

Please note, all changes are made in "config" subdirectory of your project.

web-weaver.pml
!!!!!!!!!!!!!!

This file needs to be modified to tell luban that a customized
web-weaver-library component is needed.

Add a  new line::
  
  <facility name="library">web-weaver-library</facility>

To make it sth like::

 <inventory >
  <component name="web-weaver">
    <property name="controller-url">/cgi-bin/main.py</property>
    <property name="html-base">http://localhost:8810</property>
 
    <facility name="library">web-weaver-library</facility>
  </component>
 </inventory>


web-weaver-library.odb
!!!!!!!!!!!!!!!!!!!!!!

Here we create the customized web-weaver-library component.

Create a new file web-weaver-library.odb::

 from luban.content import registerElementProvider
 registerElementProvider('chart.content')  # chart.content is the python package that contains the python definition of new luban widgets
 
 from luban.components.weaver.web.LibraryFactory import create, getCategories
 def library():
     cats = getCategories()
     Library = create(cats)
     return Library()


web-weaver-library.pml
!!!!!!!!!!!!!!!!!!!!!!

This file is used to configure the customized component.

Create a new file web-weaver-library.pml::
 
 <inventory>
 
  <component name='web-weaver-library'>
    <component name='chart'>
      <property name='stylesheets'>
	chart.css
      </property>
      <property name='javascripts'>
	protovis-r3.2.js
	chart.js
      </property>
    </component>
  </component>
  
 </inventory>


The "stylesheets" property should be a list of css files specific to
the widget, and the 'javascripts" property should be a list of
javascripts files necessary for the widget.
