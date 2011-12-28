#!/usr/bin/env python

import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy, luban

class Root:

    def __init__(self):
        from luban.weaver.web import create as createWeaver
        self.weaver = createWeaver(
            controller_url = 'helloworld',
            statichtmlbase='static')
        return

    @cherrypy.expose
    def welcome(self):
        # the overall frame
        frame = luban.e.frame(title='my application')
        # a document in the frame
        doc = frame.document(title='Hello world!', name='doc1')
        # establish interface
        action = luban.a.establishInterface(frame)
        # weave to produce html
        return self.weaver.weave(action)

    @cherrypy.expose
    def index(self):
        return "Hello"
    index.exposed = True

# cherrypy.quickstart(HelloWorld())

