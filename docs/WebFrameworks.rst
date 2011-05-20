.. _webframeworks:

Use luban with other python-based web frameworks
================================================

Luban can be combined with other python-based web frameworks at different levels.
First we will show it is easy to use luban core with any web frameworks.
The main thing to remember is that UI developers can create UI using
luban's python syntax and then convert the UI representation trees or
UI actions to html or json.


web.py
------

web.py is a simple yet powerful python web framework.

* Framework website: http://webpy.org

You will need to install web.py before the following examples work.
Usually this works::

 $ sudo easy_install web.py

Otherwise, please refer to `web.py home page <http://webpy.org>`_
for more details.

Hello world
^^^^^^^^^^^
A web.py hello world example **without** luban could look like this::
  
 #!/usr/bin/env python
 # Hello world example: run it and see it live at http://0.0.0.0:8080/helloworld
 
 import web

 urls = (
     '/helloworld', 'helloworld',
     )
 
 class helloworld:
 
     def welcome(self): return "Hello World!"
 
     def GET(self): return self.welcome()

 app = web.application(urls, globals())
 
 
 if __name__ == '__main__': app.run()

It is nice and simple. Basically all is needed is to implement the GET method to return a string.

An example **using** luban is only slightly different::
    
    #!/usr/bin/env python
    # Hello world example: run it and see it live at http://0.0.0.0:8080/helloworld
     
    import web
 
    urls = (
        '/helloworld', 'helloworld',
        )
 
    import luban.content as lc

    class helloworld:

        def __init__(self):
            from luban.weaver.web import create as createWeaver
            self.weaver = createWeaver(
                controller_url = 'helloworld',
                statichtmlbase='static')
            return

        def welcome(self):
            # the overall frame
            frame = lc.frame(title='my application')
            # a document in the frame
            doc = frame.document(title='Hello world!', id='doc1')
            # weave to produce html
            return self.weaver.weave(frame)

        def GET(self):  return self.welcome()

    app = web.application(urls, globals())

    if __name__ == '__main__': app.run()

You can see that we need a luban weaver (in the constructor),
and use the weaver to weave html output from luban representation of a UI frame
before returning from a handler.

You will need some javascript libraries to have this example working.
Please follow :ref:`instructions below <webpy-downloadandrun-examples>` 
to download a full example and try it out.


.. _webpy-downloadandrun-examples:

Download and run examples
^^^^^^^^^^^^^^^^^^^^^^^^^
Examples of using web.py with luban are available for download and play with.
Use the "download-luban-project.py" script to download an example::

 $ download-luban-project.py <projectname>

Then cd into the example project::

 $ cd <projectname>

There should be a "README" file with instructions to run the example and see it 
in browser.

For example, to download and run helloworld-web.py example project, do ::

 $ download-luban-project.py helloworld-web.py
 $ cd helloworld-web.py
 $ cat README
 $ python server.py &
 $ firefox http://0.0.0.0:8080/helloworld

Following are example projects for luban+web.py

* helloworld-web.py: hello world that communicates with controller through ajax  
  (`browse source <http://dev.danse.us/trac/luban/browser/trunk/examples/helloworld-web.py>`_)
* login-web.py: login form with error handling. shows how to use POST 
  (`browse source <http://dev.danse.us/trac/luban/browser/trunk/examples/login-web.py>`_)


Google application engine + web.py
----------------------------------

You can use luban with
`Google application engine <http://code.google.com/appengine/>`_ .

You will need to install Google application engine python SDK before the
following works.

The way of using web.py under GAE is almost identical to using web.py 
directly. You will just need to configure the GAE project to use the
controller python module based on web.py.

Luban provides a convenient way to create a skeleton GAE project that
uses web.py and luban.
You could create a luban project that works with google application engine
by::

 $ create-luban-project.py --flavor=webpy_gae <projectname>

To serve the project, use the GAE development server::

 $ dev_appserver.py <projectname>

Open http://localhost:8080 to see the project served.

